const fdk = require('@fnproject/fdk');
const fetch = require('node-fetch');

/**
 * OCI Function – ocinoti
 *
 * 触发方式：HTTP POST
 * 业务流程：
 *   a) 如果请求体中有 ConfirmationURL，则发送 GET 并直接返回
 *   b) 否则使用环境变量（corpid、corpsecret、agentid、touser）调用企业微信 API
 *   c) 返回四个环境变量的值以及（如果有）ConfirmationURL
 */
fdk.handle(async function (input) {

  // 仅允许 POST（fnproject 已经把 body 解析为对象但仍需检查 method）
  // 这里的 `input` 已经是对象，method 只能在外部 HTTP 代理层判断。
  // 为了兼容 fnproject，我们直接在代码中做业务判断：

  // 1. 读取请求体（fnproject 已经把 JSON 解析为对象）
  let body = {};
  try {
    // input 可能是已经解析好的对象，也可能是字符串（防御性写法）
    if (typeof input === 'string') {
      body = JSON.parse(input);
    } else {
      body = input;
    }
  } catch (e) {
    return {
      statusCode: 400,
      body: JSON.stringify({ code: 400, msg: '请求体不是合法 JSON' })
    };
  }

  // 2. 读取四个环境变量（永远都是字符串）
  const corpid    = process.env.corpid    || '';
  const corpsecret = process.env.corpsecret || '';
  const agentid    = process.env.agentid    || '';
  const touser     = process.env.touser     || '';

  // 3. 处理 ConfirmationURL（如果存在且非空）
  if (body.ConfirmationURL && body.ConfirmationURL.trim() !== '') {
    console.log('开始请求 ConfirmationURL:', body.ConfirmationURL);
    try {
      // 发起 GET，不关心返回值，只要不抛异常即算成功
      await fetch(body.ConfirmationURL, {
        method: 'GET',
        headers: { 'User-Agent': 'OCI-Function' }
      });
      console.log('ConfirmationURL 请求已完成');
      // 返回四个环境变量 + ConfirmationURL
      return {
        statusCode: 200,
        body: JSON.stringify({
          code: 200,
          msg: 'ConfirmationURL 请求已发送',
          corpid,
          corpsecret,
          agentid,
          touser,
          ConfirmationURL: body.ConfirmationURL
        })
      };
    } catch (e) {
      console.warn('ConfirmationURL 请求异常:', e.message);
      return {
        statusCode: 400,
        body: JSON.stringify({
          code: 400,
          msg: 'ConfirmationURL 请求失败',
          error: e.message,
          corpid,
          corpsecret,
          agentid,
          touser,
          ConfirmationURL: body.ConfirmationURL
        })
      };
    }
  }

  // 4. 如果没有 ConfirmationURL，则走企业微信消息推送逻辑
  // ---- 获取 access_token ----
  const tokenUrl = `https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=${encodeURIComponent(
    corpid)}&corpsecret=${encodeURIComponent(corpsecret)}`;

  let accessToken;
  try {
    const tokenRes = await fetch(tokenUrl);
    const tokenData = await tokenRes.json();
    if (tokenData.errcode !== 0) {
      throw new Error(`获取 token 失败：${tokenData.errmsg}（${tokenData.errcode}）`);
    }
    accessToken = tokenData.access_token;
  } catch (e) {
    console.error('获取 access_token 异常:', e.message);
    return {
      statusCode: 500,
      body: JSON.stringify({
        code: 500,
        msg: '获取企业微信 access_token 失败',
        error: e.message,
        corpid,
        corpsecret,
        agentid,
        touser
      })
    };
  }

  // ---- 发送消息 ----
  const sendUrl = `https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=${encodeURIComponent(accessToken)}`;
  const payload = {
    touser,
    msgtype: 'text',
    agentid: parseInt(agentid, 10), // 企业微信要求是数字
    text: {
      content: JSON.stringify(body, null, 2) // 把原始请求体原样发送
    }
  };

  try {
    const sendRes = await fetch(sendUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const sendResult = await sendRes.json();
    if (sendResult.errcode !== 0) {
      throw new Error(`发送失败：${sendResult.errmsg}（${sendResult.errcode}）`);
    }

    // 成功返回：四个 env + ConfirmationURL（这里为空） + 微信 API 原始返回
    return {
      statusCode: 200,
      body: JSON.stringify({
        code: 200,
        msg: '推送成功',
        corpid,
        corpsecret,
        agentid,
        touser,
        ConfirmationURL: '',
        wechatResult: sendResult
      })
    };
  } catch (e) {
    console.error('发送企业微信消息异常:', e.message);
    return {
      statusCode: 500,
      body: JSON.stringify({
        code: 500,
        msg: '发送企业微信消息失败',
        error: e.message,
        corpid,
        corpsecret,
        agentid,
        touser,
        ConfirmationURL: ''
      })
    };
  }
});
