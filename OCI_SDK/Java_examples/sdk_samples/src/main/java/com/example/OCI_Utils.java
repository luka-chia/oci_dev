package com.example;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

import com.example.s3_v2_vhost.OCIS3Demo_BasicOperator;

public class OCI_Utils {
    public static String getProperty(String key) {
        Properties props = new Properties();
        
        // 使用 ClassLoader 读取类路径下的资源文件
        try (InputStream input = OCIS3Demo_BasicOperator.class.getClassLoader()
                .getResourceAsStream("config.properties")) {
            
            if (input == null) {
                System.out.println("抱歉，未找到 config.properties 文件");
                return null;
            }

            // 加载属性列表
            props.load(input);

            // 获取并返回结果
            return props.getProperty(key);

        } catch (IOException ex) {
            ex.printStackTrace();
            return null;
        }
    }
}
