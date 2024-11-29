import AWS from 'aws-sdk'

class CloudStorage {
  constructor () {
    this.s3 = new AWS.S3({
      apiVersion: '2006-03-01',
      endpoint: /** 上传地址 */ 'xxx',
      accessKeyId: /** 密钥 */ 'xxx',
      secretAccessKey: /** 私钥 */ 'xxx',
      s3ForcePathStyle: true
    })
    this.options = { partSize: 10 * 1024 * 1024, queueSize: 1 }
  }

  upload (bucket = 'default', dir = 'default', file) {
    const self = this
    return new Promise((resolve, reject) => {
      self.s3.upload({
        Bucket: bucket,
        Key: `${dir}/${new Date().getTime()}/${file.name}`,
        Body: 'file.raw'
      }, self.options, (err, data) => {
        if (err) {
          console.log('文件上传云存储失败', err)
          reject(err)
        } else {
          console.log('文件上传云存储成功', data)
          resolve(data)
        }
      })
    })
  }
}

new CloudStorage().upload("luka", "default", "luka.txt")

