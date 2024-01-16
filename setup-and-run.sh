git switch develop
git pull
docker container stop apienvioemail
docker container rm -f apienvioemail
docker build  -t apienvioemail-v1 .
docker run --name apienvioemail apienvioemail-v1