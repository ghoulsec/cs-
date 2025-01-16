# cs上线消息提醒
由公开项目修改而来，达到简易的上线提醒(钉钉机器人)

使用说明
实验环境为4.9.1
如果是本地添加cna文件可能无法及时收到上线消息，所以需要在服务器上将脚本挂在后台使用。
1，将脚本内容的token修改为你自己的机器人token值
2，使用该命令创建agscript文件
echo "java -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -javaagent:uHook.jar -classpath ./cobaltstrike-client.jar aggressor.headless.Start \$*" > agscript
3，建立screen后台
./agscript ip port username password /path/上线.cna

