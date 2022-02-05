# songs-i-like-api

Developed to mess around with APIs and songs that I like.

https://songs-i-like.herokuapp.com/

FastAPI, Postgres are used.

<br/><br/>
Example project will be here soon:

#songoftheday

<br/><br/>
## Endpoints
>Can be viewed in [/docs](https://songs-i-like.herokuapp.com/docs)

### GET /api/songs

Brings all songs saved.

Curl
```
curl -X 'GET' \
  'https://songs-i-like.herokuapp.com/api/songs' \
  -H 'accept: application/json'
```

Example response: 200 OK
```
[
    {
        "id":1,
        "artistName":"Men I Trust",
        "songName":"Lauren"
    },
    {
        "id":2,
        "artistName":"Tame Impala",
        "songName":"The Less I Know the Better"
    },
    ...
]
```
<br/><br/>
### POST /api/songs

Adds a new song.

Example request body:
```
{
  "artistName": "Mor ve Otesi",
  "songName": "Bazen"
}
```
Then response: 201 Created
```
{
  "id": 57,
  "artistName": "Mor ve Otesi",
  "songName": "Bazen"
}
```
<br/><br/>
### PUT /api/songs/{song_id}

Updates a song with id.

Example request body:
```
PUT /api/song/57
{
  "artistName": "Mor ve Otesi",
  "songName": "Gul Kendine"
}
```
Then response: 200
```
{
  "id": 57,
  "artistName": "Mor ve Otesi",
  "songName": "Gul Kendine"
}
```
<br/><br/>
### DELETE /api/songs/{song_id}

Deletes a song with id.

Example request:
```
curl -X 'DELETE' \
  'https://songs-i-like.herokuapp.com/api/song/57' \
  -H 'accept: application/json'
```
Then response: 200
```
{
  "artistName": "Mor ve Otesi",
  "songName": "Gul Kendine",
  "id": 57
}
```