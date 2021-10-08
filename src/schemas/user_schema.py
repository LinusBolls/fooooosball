from .atomics_schema import created_schema, email_schema

user_schema = {
    "bsonType": "object",
    "additionalProperties": True,
    "required": [ "email", "created" ],
    "properties": {
        "created": created_schema,
        "email": email_schema,
        "name": {
            "bsonType": "string",
            "description": "Nickname, optional"
        },
        "img": {
            "bsonType": "string",
            "description": "Profile picture url, optional"
        },
        "matches": {
            "bsonType": [ "array" ],
            "items": {
                "bsonType": "string",
                "description": "Match id"
            },
            "description": "The matches the user has played"
        }
    }
}