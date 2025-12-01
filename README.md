# \# Social Media Disaster Data Repository

# 

# This repository contains \*\*open-source datasets\*\* collected from publicly available sources that capture social media activity and disaster-related information. The project focuses on \*\*scraping textual data from these datasets and creating API endpoints\*\* for easy access and analysis.

# 

# > Note: Not all datasets listed are directly used in this project. They are included for reference and to assist researchers in locating relevant datasets.

# 

# \## Datasets Included (Reference)

# 

# | File Name                                                                | Description                                                             |

# | ------------------------------------------------------------------------ | ----------------------------------------------------------------------- |

# | `countries-countries-fb-social-connectedness-index-october-2021.tsv`     | Facebook Social Connectedness Index for countries (Oct 2021).           |

# | `crisismmd\_datasplit\_agreed\_label.zip`                                   | CrisisMMD dataset with agreed labels for multimodal social media posts. |

# | `crisismmd\_datasplit\_all.zip`                                            | Full CrisisMMD dataset with all labeled posts.                          |

# | `CrisisMMD\_raw\_tweets\_ids.tar.gz`                                        | Raw tweet IDs from CrisisMMD dataset.                                   |

# | `CrisisMMD\_v1.0.tar.gz`                                                  | Version 1.0 of the CrisisMMD multimodal social media dataset.           |

# | `CrisisMMD\_v2.0.tar.gz`                                                  | Version 2.0 of the CrisisMMD multimodal social media dataset.           |

# | `CrisisNLP\_labeled\_data\_crowdflower\_v2.zip`                              | Labeled social media posts collected via CrowdFlower for NLP tasks.     |

# | `CrisisNLP\_volunteers\_labeled\_data.zip`                                  | Labeled posts from volunteers for NLP research.                         |

# | `FloodsInPakistan-tweets.csv.zip`                                        | Tweets related to flood events in Pakistan.                             |

# | `FloodsInPakistan2022-tweets.csv.zip`                                    | Tweets specifically from Pakistan flood events in 2022.                 |

# | `gadm1\_nuts3\_counties-fb-social-connectedness-index-october-2021.zip`    | County-level Facebook Social Connectedness Index dataset.               |

# | `HumAID\_data\_all\_combined.tar.gz`                                        | Complete HumAID dataset for humanitarian aid social media posts.        |

# | `HumAID\_data\_events\_set1\_47K.tar.gz`                                     | First subset of HumAID event-labeled data.                              |

# | `HumAID\_data\_events\_set2\_29K.tar.gz`                                     | Second subset of HumAID event-labeled data.                             |

# | `HumAID\_data\_event\_type.tar.gz`                                          | Event-type-specific labeled data from HumAID.                           |

# | `OOV\_Dict.zip`                                                           | Dictionary of out-of-vocabulary words for NLP tasks.                    |

# | `PakistanFloodsAppeal-tweets.csv.zip`                                    | Tweets related to humanitarian appeals during Pakistan floods.          |

# | `us-counties-countries-fb-social-connectedness-index-october-2021.tsv`   | US county-level Facebook Social Connectedness Index data.               |

# | `us-counties-us-counties-fb-social-connectedness-index-october-2021.zip` | Social connectedness index across US counties.                          |

# | `us-zip-code-us-zip-code-fb-social-connectedness-index-october-2021.zip` | Social connectedness index across US ZIP codes.                         |

# 

# \## Source \& License

# 

# All datasets are \*\*open-source\*\* and have been collected from publicly available repositories online. They are intended for research, analysis, and educational purposes. Please refer to the respective dataset providers for specific licensing details.

# 

# \## Usage

# 

# These datasets and endpoints can be used for:

# 

# \* Social media analytics during disaster events

# \* Crisis communication studies

# \* Disaster risk assessment and early warning systems

# \* NLP, sentiment analysis, and multimodal AI research

# \* Humanitarian aid coordination and response studies

# 

# \### Example: Accessing an Endpoint

# 

# ```python

# import requests

# 

# response = requests.get('http://localhost:8000/api/disasters')

# data = response.json()

# print(data\[:5])

# ```

# 

# \## References

# 

# \* Erokhin \& Komendantova, \*Social media data for disaster risk management and research\*, 2024【9†source】

# \* Akbar et al., \*Crisis Communication Effectiveness in Disaster Management\*, 2025【10†source】

# \* Cantini et al., \*Prompt-based LLMs for disaster monitoring\*, 2025【11†source】

# \* Xiao et al., \*Social Media-Enabled Flood Disaster Informatics\*, 2025【12†source】

# \* NDMA Live Disaster Intelligence Dashboard, 2025【13†source】

# 

# \## Citation

# 

# If you use these datasets or endpoints, please cite the original sources appropriately.



