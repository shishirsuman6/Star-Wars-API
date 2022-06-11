"""
The purpose of this file is to store the message schemas to use the pytest framework for Start Wars API
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
import json
from jsonschema import validate


#--------------------------------------------------------------------
# Schemas
#--------------------------------------------------------------------

schema_people = {
    "description": "A person within the Star Wars universe",
    "title": "People",
    "required": [
        "name",
        "height",
        "mass",
        "hair_color",
        "skin_color",
        "eye_color",
        "birth_year",
        "gender",
        "homeworld",
        "films",
        "species",
        "vehicles",
        "starships",
        "url",
        "created",
        "edited"
    ],
    "$schema": "http://json-schema.org/draft-04/schema",
    "type": "object",
    "properties": {
        "starships": {
            "type": "array",
            "description": "An array of starship resources that this person has piloted"
        },
        "edited": {
            "type": "string",
            "description": "the ISO 8601 date format of the time that this resource was edited.",
            "format": "date-time"
        },
        "name": {
            "type": "string",
            "description": "The name of this person."
        },
        "created": {
            "type": "string",
            "description": "The ISO 8601 date format of the time that this resource was created.",
            "format": "date-time"
        },
        "url": {
            "type": "string",
            "description": "The url of this resource",
            "format": "uri"
        },
        "gender": {
            "type": "string",
            "description": "The gender of this person (if known)."
        },
        "vehicles": {
            "type": "array",
            "description": "An array of vehicle resources that this person has piloted"
        },
        "skin_color": {
            "type": "string",
            "description": "The skin color of this person."
        },
        "hair_color": {
            "type": "string",
            "description": "The hair color of this person."
        },
        "height": {
            "type": "string",
            "description": "The height of this person in meters."
        },
        "eye_color": {
            "type": "string",
            "description": "The eye color of this person."
        },
        "mass": {
            "type": "string",
            "description": "The mass of this person in kilograms."
        },
        "films": {
            "type": "array",
            "description": "An array of urls of film resources that this person has been in."
        },
        "species": {
            "type": "array",
            "description": "The url of the species resource that this person is."
        },
        "homeworld": {
            "type": "string",
            "description": "The url of the planet resource that this person was born on."
        },
        "birth_year": {
            "type": "string",
            "description": "The birth year of this person. BBY (Before the Battle of Yavin) or ABY (After the Battle of Yavin)."
        }
    }
}


schema_people_wrong = {
    "description": "A person within the Star Wars universe",
    "title": "People",
    "required": [
        "name",
        "height",
        "mass",
        "hair_color",
        "skin_color",
        "eye_color",
        "birth_year",
        "gender",
        "homeworld",
        "films",
        "species",
        "vehicles",
        "starships",
        "url",
        "created",
        "edited",
        "xyz"
    ],
    "$schema": "http://json-schema.org/draft-04/schema",
    "type": "object",
    "properties": {
        "starships": {
            "type": "array",
            "description": "An array of starship resources that this person has piloted"
        },
        "edited": {
            "type": "string",
            "description": "the ISO 8601 date format of the time that this resource was edited.",
            "format": "date-time"
        },
        "name": {
            "type": "string",
            "description": "The name of this person."
        },
        "created": {
            "type": "string",
            "description": "The ISO 8601 date format of the time that this resource was created.",
            "format": "date-time"
        },
        "url": {
            "type": "string",
            "description": "The url of this resource",
            "format": "uri"
        },
        "gender": {
            "type": "string",
            "description": "The gender of this person (if known)."
        },
        "vehicles": {
            "type": "array",
            "description": "An array of vehicle resources that this person has piloted"
        },
        "skin_color": {
            "type": "string",
            "description": "The skin color of this person."
        },
        "hair_color": {
            "type": "string",
            "description": "The hair color of this person."
        },
        "height": {
            "type": "string",
            "description": "The height of this person in meters."
        },
        "eye_color": {
            "type": "string",
            "description": "The eye color of this person."
        },
        "mass": {
            "type": "string",
            "description": "The mass of this person in kilograms."
        },
        "films": {
            "type": "array",
            "description": "An array of urls of film resources that this person has been in."
        },
        "species": {
            "type": "array",
            "description": "The url of the species resource that this person is."
        },
        "homeworld": {
            "type": "string",
            "description": "The url of the planet resource that this person was born on."
        },
        "birth_year": {
            "type": "string",
            "description": "The birth year of this person. BBY (Before the Battle of Yavin) or ABY (After the Battle of Yavin)."
        }
    }
}
