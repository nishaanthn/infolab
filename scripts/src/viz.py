'''
For a simple visualization using d3
'''
from tweets_processor import get_tweets
import cjson
import os
import sys



def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def count_country_names(tweets, country_counter):
  for t in tweets:
    if "place" in t:
      if t["place"]:
        #print t["place"]["country"]
        if t["place"]["country"] not in country_counter:
            country_counter[t["place"]["country"]] = 1
        else:
            country_counter[t["place"]["country"]] += 1
      
          
  
  for b in country_counter:
    print b, country_counter[b]
  
      
def count_software_occurence(tweets, software_counter):
  for t in tweets:
    if "text" in t:
      #your shit goes here
      
      if t["source"] == "web":
        software_counter["Web"] += 1

      else:
        brokendownsource = t["source"].split("nofollow\">")
        tempsoftware = brokendownsource[1].split("</a")
        if " BlackBerry" in tempsoftware[0]:
          tempsoftware[0] = "Blackberry"
        elif " iOS" in tempsoftware[0]:
          tempsoftware[0] = "iOS"
        elif " Android" in tempsoftware[0]:
          tempsoftware[0] = "Android"
        elif " iPhone" in tempsoftware[0]:
          tempsoftware[0] = "iPhone"
        elif " Mac" in tempsoftware[0]:
          tempsoftware[0] = "Mac"
        elif " iPad" in tempsoftware[0]:
          tempsoftware[0] = "iPad"
        elif " Windows Phone" in tempsoftware[0]:
          tempsoftware[0] = "Windows Phone"
        elif "." in tempsoftware[0]:
          tempsoftware[0] = "Social Media Plugin"
        if tempsoftware[0] not in software_counter:
          software_counter[tempsoftware[0]] = 1
        else:
          software_counter[tempsoftware[0]] += 1
      """
			if ":)" in t["text"] or ":-)" in  t["text"]:
				expressions_hash["happy"]["val"] += 1
			elif ":(" in t["text"] or ":-(" in t["text"] or ":'(" in t["text"]:
				expressions_hash["sad"]["val"] += 1
			elif ":o" in t["text"] or ":O" in t["text"]:
				expressions_hash["surprised"]["val"] += 1
			elif ";)" in t["text"] or ";-)" in t["text"]:
				expressions_hash["wink"]["val"] += 1
        """
  for i in software_counter:
    if software_counter[i] <= 10:
      software_counter = removekey(software_counter, i)
      
  for i in software_counter:
    print i, software_counter[i]
  """
  f = open("exprs.json", "w")
  expressions = []
  for a in expressions_hash:
    expressions.append(expressions_hash[a])
  f.write(cjson.encode(expressions))
  f.close()
  print expressions_hash
  """

def main():
  dict_of_software_counts = {"Web":0}
  dict_of_country_names = {}
  for i in os.listdir(sys.argv[1]):
    if i.endswith(".txt"):
      in_file = sys.argv[1] + i  
      tweets = get_tweets(in_file)
      #count_software_occurence(tweets, dict_of_software_counts)
      count_country_names(tweets, dict_of_country_names)
  

if __name__ == "__main__":
  main()
