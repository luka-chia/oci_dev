<template>
    <div class="about">
        <div style="display: flex;justify-content: center;align-items: center;">
            <el-form label-position="left" label-width="120px" :model="s3Clent" style="width:500px">
                <el-form-item label="endpoint">
                    <el-input v-model="s3Clent.endpoint"></el-input>
                </el-form-item>
                <el-form-item label="region">
                    <el-input v-model="s3Clent.region"></el-input>
                </el-form-item>
                <el-form-item label="signatureVersion">
                    <el-input v-model="s3Clent.signatureVersion"></el-input>
                </el-form-item>
                <el-form-item label="bucket">
                    <el-input v-model="s3Clent.bucket"></el-input>
                </el-form-item>
                <el-form-item label="accessKeyId">
                    <el-input v-model="s3Clent.credentials.accessKeyId"></el-input>
                </el-form-item>
                <el-form-item label="secretAccessKey">
                    <el-input v-model="s3Clent.credentials.secretAccessKey"></el-input>
                </el-form-item>
            </el-form>
            
        </div>
        <div style="margin:20px 0px 20px 0px">
            <el-button @click="sureS3()">确定</el-button>
        </div>
        <input multiple v-show="false" ref="fileRef" type="file" @change="inputFile">
        <el-button type="primary" @click="upload()">点击上传文件</el-button>
        <el-button type="primary" @click="getFileList()">获取存储桶文件列表</el-button>

        <div v-for="f in fileList" :key="f.key">
            <div style="margin-top:50px;display: flex;align-items: center;justify-content: center;" v-if="f.show">
                <div style="margin-right:20px;font-size:15px;font-weight:60">
                    {{ f.key }}
                </div>
                <el-progress :percentage="f.percentage" style="width:500px"></el-progress>
                <div style="margin-left:20px">
                    <span v-if="f.status == 'err'" style="color:#F56C6C">上传错误</span>
                    <span v-else-if="f.status == 'same key'" style="color:#F56C6C">同名文件</span>
                    <span v-else-if="f.status == 'success'" style="color:#67C23A">上传成功</span>
                    <span v-else-if="f.status == 'suspend'" style="color:#409EFF">已暂停</span>
                </div>
                <div style="margin-left:20px">
                    <!-- 暂停按钮 -->
                    <el-button type="primary" icon="el-icon-video-pause" circle v-if="f.status === 'wait'"
                        @click="suspendButton(f)"></el-button>
                    <!-- 继续按钮 -->
                    <el-button type="primary" icon="el-icon-video-play" circle v-if="f.status === 'suspend'"
                        @click="continuedButton(f)"></el-button>
                    <!-- 取消按钮 -->
                    <el-button type="danger" icon="el-icon-close" circle v-if="f.status === 'suspend' || f.status === 'err'"
                        @click="cancelButton(f)"></el-button>
                    <!-- 重试按钮 -->
                    <el-button type="primary" icon="el-icon-refresh-right" circle v-if="f.status === 'err'"
                        @click="continuedButton(f)"></el-button>
                </div>
            </div>
        </div>

        <ul>

            <li v-for="item in listFile" >{{ item }}</li>

            </ul>
    </div>
</template>

<script>
import { init, cancel, fileChange, getWorker,getObjectList } from '../assets/js/s3.js'
export default {
    data() {
        return {
            fileList: [],//存储上传文件列表
            s3Clent: {
                endpoint: "https://sehubjapacprod.compat.objectstorage.us-ashburn-1.oraclecloud.com",
                region: 'us-ashburn-1',
                s3ForcePathStyle: true,
                signatureVersion: 'v4',
                forcePathStyle: true,
                bucket:'Luka-bucket-ashburn',
                credentials: {
                    accessKeyId: '9ad2bd61577c54806037d381fbb7fb9be54a4eba',
                    secretAccessKey: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                },
            
            },//s3配置文件
            init_yes:false,
            listFile:[],
        }
    },
    methods: {
        async continuedButton(file) {
            file.needSuspend = false;
            file.status = 'wait';
            const isInQueue = getWorker(file.key);
            console.log("isInQueue", isInQueue)
            if (isInQueue === false) {
                //如果任务队列中没有这个文件上传任务，那么就加入到任务队列中
                let inputFile = {
                    key: file.key,//文件对象名(一般为文件的名称，也可根据需求自定)
                    percentage: file.percentage,
                    status: file.status,
                    show: file.show,
                    file: file.file,
                    needSuspend: file.needSuspend,
                    sharding: file.sharding,//分片数组
                    shardSize: file.shardSize//每个分片的大小
                }
                fileChange({ fileList: [inputFile], bucket: this.s3Clent.bucket, changeStatus: this.changeStatus, getSuspend: this.getSuspend, changeSharding: this.changeSharding });
            }

        },
        async cancelButton(f) {
            let result = await cancel({ bucket: this.s3Clent.bucket, fKey: f.key });
            if (result == true) {
                this.fileList = this.fileList.filter(e => {
                    return e.key !== f.key;
                });
            }
        },
        upload() {
            if(!this.init_yes)
            {
                alert('先初始化客户端');
                return;
            };
            this.$refs.fileRef.dispatchEvent(new MouseEvent('click'));
        },

        getFileList(){
            
            
            const listFile = getObjectList(this.s3Clent);

           
            listFile.then(res=> this.listFile = res)

        //    listFile.then(res=> this.listFile = res)
            
            

        },
        inputFile(event) {
            if (this.s3Clent.credentials.accessKeyId == "xxxxxx") {
                init(this.s3Clent);
            }
            let files = event.target.files;
            let addFile = [];
            for (let i = 0; i < files.length; i++) {
                this.fileList.push({
                    key: files[i].name,//文件对象名(一般为文件的名称，也可根据需求自定)
                    percentage: 0,
                    status: 'wait',
                    show: true,
                    file: files[i],
                    needSuspend: false,
                    sharding: [],//分片数组
                    shardSize: 32 * 1024 * 1024//每个分片的大小
                });
                addFile.push({
                    key: files[i].name,//文件对象名(一般为文件的名称，也可根据需求自定)
                    percentage: 0,
                    status: 'wait',
                    show: true,
                    file: files[i],
                    needSuspend: false,
                    sharding: [],//分片数组
                    shardSize: 32 * 1024 * 1024//每个分片的大小
                });
            }
            fileChange({ fileList: addFile, bucket: this.s3Clent.bucket, changeStatus: this.changeStatus, getSuspend: this.getSuspend, changeSharding: this.changeSharding })
        },
        //暂停
        suspendButton(file) {
            file.needSuspend = true;
            file.status = 'suspend';
        },
        //修改状态
        changeStatus(key, val) {
            console.log('val')
            for (let i = 0; i < this.fileList.length; i++) {
                if (this.fileList[i].key == key) {
                    this.fileList[i].status = val;
                    if (val === 'success') {
                        this.fileList[i].percentage = 100;
                    }
                    break;
                }
            }
        },
        //修改分片数组
        changeSharding(key, shard) {
            for (let i = 0; i < this.fileList.length; i++) {
                if (this.fileList[i].key === key) {
                    this.fileList[i].sharding = shard;
                    //改变进度条
                    let size = 0;
                    for (let j = 0; j < shard.length; j++) {
                        size += shard[j].Size;
                    }
                    this.fileList[i].percentage = ((size / this.fileList[i].file.size) * 100).toFixed(1) - 0;
                    return;
                }
            }
        },
        //获取该文件是否需要暂停
        getSuspend(key) {
            let suspend = this.fileList.filter(e => {
                return e.key === key;
            });
            if (suspend.length != 0) {
                return suspend[0].needSuspend;
            }
            return false;
        },
        sureS3() {
            //创建客户端
            init(this.s3Clent);
            this.init_yes=true;
        }

    },
    created() {

    }
}
</script>