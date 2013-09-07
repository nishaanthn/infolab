'''
For a simple visualization using d3
'''
from tweets_processor import get_tweets
import cjson

def count_expressions(tweets):
	expressions_hash = {"happy": {"pic": ":)", "val": 0},
                      "sad": {"pic": ":(", "val": 0},
                      "surprised": {"pic": ":o", "val": 0},
											"wink": {"pic": ";)", "val": 0}
                     }
	for t in tweets:
		if "text" in t:
			if ":)" in t["text"]:
				expressions_hash["happy"]["val"] += 1
			elif ":(" in t["text"]:
				expressions_hash["sad"]["val"] += 1
			elif ":o" in t["text"] or ":O" in t["text"]:
				expressions_hash["surprised"]["val"] += 1
			elif ";)" in t["text"]:
				expressions_hash["wink"]["val"] += 1
	f = open("exprs.json", "w")
	expressions = []
	for a in expressions_hash:
		expressions.append(expressions_hash[a])
	f.write(cjson.encode(expressions))
	f.close()
	print expressions_hash

def main():
	in_file = "/home/vandana/Dropbox/codinggig/data/sample/geo.2013-08-26_23-45.txt"
	tweets = get_tweets(in_file)
	count_expressions(tweets)

if __name__ == "__main__":
  main()
