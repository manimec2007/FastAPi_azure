from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import json


s = """{
"company":"the natori company",

"profile":[
		{"value":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Mrs._Natori_portrait2.JPG/800px-Mrs._Natori_portrait2.JPG",
		  "score":"0.98",
		  "link":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Mrs._Natori_portrait2.JPG/800px-Mrs._Natori_portrait2.JPG"
		  },
		  {
		  "value":"https://media-exp1.licdn.com/dms/image/C4E03AQGPYzZVTglO3w/profile-displayphoto-shrink_400_400/0/1516176053249?e=1659571200&v=beta&t=xs3RrMAY80cfUXyUCEQJCdm04AG9389-I1dk9K2dYH0",
		  "score":"0.87",
		  "link":"https://media-exp1.licdn.com/dms/image/C4E03AQGPYzZVTglO3w/profile-displayphoto-shrink_400_400/0/1516176053249?e=1659571200&v=beta&t=xs3RrMAY80cfUXyUCEQJCdm04AG9389-I1dk9K2dYH0"
		  }],

"name":[{"value":"josie natori",
		"score":"1.0",
		"link":"https://en.wikipedia.org/wiki/Josie_Natori"
		},
		{"value":" ken natori",
		"score":"1.0",
		"link":"https://rocketreach.co/ken-natori-email_18823547"
		}
		],
"position":[{"value":"ceo",
			"score":"0.93",
			"link":"https://en.wikipedia.org/wiki/Josie_Natori"
			},
			{"value":"president",
			"score":"0.95",
			"link":"https://rocketreach.co/ken-natori-email_18823547"
			}],
"birthplace":[{"value":"manila",
				"score":"1.0",
				"link":"https://en.wikipedia.org/wiki/Josie_Natori"
				},
				{"value":"new york",
				"score":"1.0",
				"link":"https://rocketreach.co/ken-natori-email_18823547"
				}],
"dob":[{"value":"may 9 , 1947",
		"score":"1.0",
		"link":"https://en.wikipedia.org/wiki/Josie_Natori"
		},
		{"value":"0000",
		"score":"0.0",
		"link":"unknown"
		}],
"gender":["F","M"],
"maritalstatus":["married","married"],
"race":["black","white"],
"ethnicity":["filipino","filipino"],
"education":["economics","phd"],
"language":["english","english"],
"nationality":["american","american"],
"disability":["",""],
"iswomenowned":["Yes","Yes"],
"diversity":["pacific","pacific"]
}"""


def get_businessdata(text):
    data = json.loads(s)
    return data
  

app = FastAPI()


@app.get('/')
def index():
    return "Diversity Model NLP enpoint service"

@app.get('/nlp')
def get_businessinfo(businessname:str):
    res = get_businessdata(businessname)
    return res
