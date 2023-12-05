import re

knowledge_base = {
    "collections": "we have latest collection in variety of clothing brands ",
    "brands": "we have collection from brands like raymonds,siyaram's,peter england,levi's,louis phillipe and more.",
    "jeans": "we have denim jeans,crop jeans,ripped jeans",
    "T-shirts": "we have T-shirt collection from levi's,nike,adidas,puma,versace etc.",
    "size": "we have clothing available in sizes - S,M,L,XL,XXL,XXXL",
    "men": "men collection includes formal shirts,t-shirts,formalwear,partywear",
    "women": "women collection incluedes saree,jeans,skirt,coat,jacket,scarf,dress",
    "delievery": "we offer delivery across all cities in maharashtra your order will reach in 3-5 days",
    "contact": "you can reach us at (020)-738-0601",
    "price": "pricing varies from brands to brands and depends on size you select",
    "wedding wear": "for men we have sherwani,kurtas,suits and more for women we have lehanga,bridal dress,saree,gown"
}


def chatbot_response(query):
    for pattern, response in knowledge_base.items():
        if re.search(pattern, query, re.IGNORECASE):
            return response
    return "sorry! I can't find you the right answer"


def chat():
    print("Chatbot: Hii! How can I help you ? ")
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["exit", "bye", "quit"]:
            print("Good bye! have a good day")
            break
        response = chatbot_response(user_input)
        print("Chatbot: ", response)


if __name__ == "__main__":
    chat()