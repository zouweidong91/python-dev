# docker宿主机执行本
echo "This script should be run on docker host"

mkdir -p /data/es
chown -R 1000:1000 /data/es

echo "Done. Run docker-compose up latter."