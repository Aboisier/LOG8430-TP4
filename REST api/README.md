# Readme

## Running the server

Rename the `.env.example` file to `.env` and set the environment variables with your values.

Then, execute the following commands
```
npm i
npm run serve
```

## Api

### Add receipt

```cURL
curl -X POST \
  'http://localhost:3000' \
  -H 'Content-Type: application/json' \
  -d '{ "id": "c534cf02-e8f3-11e8-9f32-f2801f1b92d1", 
        "products": { "Tomato": 10, "Banana": 123 }  
      }'
```

### Get products

```cURL
curl -X GET 'http://localhost:3000'
```

### Get frequent products

```cURL
curl -X GET 'http://localhost:3000/frequent'
```