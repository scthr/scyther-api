# scyther-api

Scyther API

# Development

## Install requirements

Uses [pipenv](https://pipenv.pypa.io).

```bash
make install-dev
```

## Run test server

```bash
make run
```

## Run linter

```bash
make lint
```

## Run autoformatter

```bash
make format
```

## Test events

Podłącz się do event streamu:

```
curl localhost:8000/events/
```

Postnij ruch do endpointu ``move/`` i ogłoś koniec wieku niewinnośći:

```
curl -XPOST localhost:8000/api/move/ -d '{"actions": ["Handel dwie ropy bez dolnej"]}'
```
