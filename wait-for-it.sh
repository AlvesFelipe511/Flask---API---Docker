#!/usr/bin/env bash

host="$1"
shift
cmd="$@"

until nc -z "$host" 5432; do
  echo "Aguardando o banco de dados em $host..."
  sleep 1
done

echo "Banco disponível — iniciando aplicação!"
exec $cmd
