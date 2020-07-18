## User (Customer)

### 가입

- `POST /auth/signUp`
- Request Body :

```json
{
  "username": "namename", # string
	"phoneNumber": "010-1111-2222", # string
  "password": "pass" # string
}
```

- Response

```json
{
	"username": "namename", # string
	"phoneNumber": "010-1111-2222", # string
  "id": 123232323, # long
  "token": "toklfnelkfnwlekfnewoignwignoinlnk" # string
}
```

### 로그인

- `POST /auth/signIn`
- Request Body :

```json
{
  "username": "namename",
  "password": "pass"
}
```

- Response

```json
{
	"username": "namename", # string
	"phoneNumber": "010-1111-2222", # string
  "id": 123232323, # long
  "token": "toklfnelkfnwlekfnewoignwignoinlnk"
}
```

## Store

### 조회

- `GET /stores`
- Request Header

```json
{
  "Authorization": "adjlkfjdldfjld"
}
```

- Response

```json
{
    "store": {
        "live": [
            {
                "name": "STORE",
                "address": "서울시~",
                "phoneNumber": "02-1214-1513",
                "category": "중식",
                "channelId": "aaaa.bbb.ccc",
                "menu": [
                    {
                        "name": "food1",
                        "price": 15000,
                        "description": "맛있",
                        "lastCookVideoUrl": "https://sknflkf"
                    },
                    {
                        "name": "food1",
                        "price": 15000,
                        "description": "맛있",
                        "lastCookVideoUrl": "https://sknflkf"
                    }
                ]
            },
            {
                "name": "STORE",
                "address": "서울시~",
                "phoneNumber": "02-1214-1513",
                "category": "중식",
                "channelId": "aaaa.bbb.ccc",
                "menu": [
                    {
                        "name": "food1",
                        "price": 15000,
                        "description": "맛있",
                        "lastCookVideoUrl": "https://sknflkf"
                    },
                    {
                        "name": "food1",
                        "price": 15000,
                        "description": "맛있",
                        "lastCookVideoUrl": "https://sknflkf"
                    }
                ]
            }
        ],
        "all" : [
            {
                "name": "STORE",
                "address": "서울시~",
                "phoneNumber": "02-1214-1513",
                "category": "중식",
                "channelId": "aaaa.bbb.ccc",
                "menu": [
                    {
                        "name": "food1",
                        "price": 15000,
                        "description": "맛있",
                        "lastCookVideoUrl": "https://sknflkf"
                    },
                    {
                        "name": "food1",
                        "price": 15000,
                        "description": "맛있",
                        "lastCookVideoUrl": "https://sknflkf"
                    }
                ]
            }
        ]
    }
}
```

## Order

### 주문 조회

- `GET /orders`
- Request Header:

```json
{
  "Authorization": "1212121212121
}
```

- Response

```json
{
    "orders": {
        "live": [
            {
                "storeId": 123121,
                "menus": [
                    "menuname",
                    "menuname2"
                ],
                "secondsLeft":  3000,
                "channelId": "djflkdjkfl"
            },
            {
                "storeId": 123121,
                "menus": [
                    "menuname",
                    "menuname2"
                ],
                "secondsLeft":  3000,
                "channelId": "djflkdjkfl"
            }
        ],
        "all" : [
            {
                "storeId": 123121,
                "menus": [
                    "menuname",
                    "menuname2"
                ]
            }
        ]
    }
}
```

### 주문 하기

- `POST /order`
- Request Header:

```json
{
  "Authorization": "1212121212121
}
```

- Request Body:

```json
{
    "storeId": 123121,
    "menus": [
        "menuname",
        "menuname2"
    ]
}
```

- Response:

```json
{
    "storeId": 123121,
    "menus": [
        "menuname",
        "menuname2"
    ],
    "secondsLeft":  3000,
    "ordersLeft": 14
}
```