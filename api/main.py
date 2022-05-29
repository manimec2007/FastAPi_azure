from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd

j = [["Park Avenue Building & Roofing Supplies, LLC",0,"HISPANIC","MBE","BOB GROENINGER","CHIEF EXECUTIVE OFFICER"],["Park Avenue Building & Roofing Supplies, LLC",0,"HISPANIC","MBE","RAYMOND RIVERA","PRESIDENT"],["Great Performances\\/Artists As Waitresses, Inc.",1,"NON-MINORITY","WBE","DEAN MARTINUS P","PRESIDENT"],["Great Performances\\/Artists As Waitresses, Inc.",1,"NON-MINORITY","WBE","LIZBETH NEUMARK","CEO"],["Upstate Rebar, LLC",1,"NON-MINORITY","WBE","BONNIE CHMIELOWIEC","MANAGING MEMBER"],["V3gate, LLC",0,"HISPANIC","MBE","OSCAR T VALDEZ JR","CHIEF EXECUTIVE OFFICER"],["V3gate, LLC",0,"HISPANIC","MBE","TAD RZONCA PRESID","DENT"],["Montana Datacom, Inc.",1,"NON-MINORITY","WBE","JENNIFER MUHLRAD","PRESIDENT"],["Montana Datacom, Inc.",1,"NON-MINORITY","WBE","STEVEN MEYERSON "," CHIEF FINANCIAL OFFICER"],["Ergonomic Group Inc.",1,"NON-MINORITY","WBE","KAREN GIRARDS","CHB"],["Ergonomic Group Inc.",1,"NON-MINORITY","WBE","SAYLE ROBERTS","CHIEF FINANCIAL OFFICER"],["22nd Century Technologies, Inc.",0,"ASIAN","MBE","SATVINDER SINGH","PRES"],["Liftforward, Inc.",0,"BLACK","MBE","JEFFREY ROGERS","CEO"],["Corporate Computer Solutions, Inc.",1,"NON-MINORITY","WBE","ANN MARTINO","PRESIDENT"],["Prwt Services, Inc.",0,"BLACK","MBE","DON PELOSO C","CHIEF FINANCIAL OFFICER"],["Prwt Services, Inc.",0,"BLACK","MBE","MALIK MAJEED","CEO"],["Talson Solutions, LLC",0,"BLACK","MBE","ROBERT S BRIGHT","MANAGING MEMBER"],["Northeast Remsco Construction, Inc.",0,"HISPANIC","MBE","JUAN GUTIERREZ","CHM"],["Northeast Remsco Construction, Inc.",0,"HISPANIC","MBE","ROLANDO ACOSTA","PRESIDENT"],["Mvp Consulting Plus, Inc.",0,"ASIAN","MWBE","ILAKUMARI N PATEL","CHIEF EXECUTIVE OFFICER"]]

cols = ['BusinessName', 'isWomenOwned', 'OwnershipType', 'DiverseType','LeaderName', 'Designation']


j = """{
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
    ndf = pd.DataFrame(columns=cols)
    for i in j:
        if i[0] == text:
            tmp=pd.DataFrame([i],columns=cols)
            ndf = ndf.append(tmp,ignore_index = True)
    data = json.loads(j)
    return data
  

app = FastAPI()


@app.get('/')
def index():
    return "Diversity Model NLP enpoint service"

@app.get('/nlp')
def get_businessinfo(businessname:str):
    res = get_businessdata(businessname)
    return res
