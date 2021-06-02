echo 'Building django-authentication-mistery'

docker rm -f django-auth &> /dev/null && \
  docker-compose up --remove-orphans --force-recreate --build -d $*
