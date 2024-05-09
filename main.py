from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI()


@app.route('/survey', methods=['POST'])
def generate_post():
    data = request.get_json()
    role = data.get('role')
    goal = data.get('goal')

    if goal is None and role is not None:
        return jsonify({'error': 'Role and goal must be provided.'}), 400

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": f""""
                    As a {role}, your objective is to help your company grow with your creative and innovative surveys. 
                    Design a survey to gather insights that will aid in achieving this goal.
                    Here are few samples:
                    
                    Role: Salesforce B2B Sales Representative
                    Goal: Conduct a quarterly survey of 100 financial services decision-makers to create sales content.
                    Survey Questions:

                        What factors influence your decision-making process when considering new solutions/providers in the financial services sector?
                        How satisfied are you with the current offerings in the market for [specific product/service]?
                        What challenges do you face in implementing new solutions within your organization?
                        How likely are you to recommend our product/service to a colleague or peer in the industry?
                        What additional features or improvements would you like to see in our product/service?
                        How frequently do you seek out new solutions/providers for your business needs?
                        
                    
                    Role: Glossier B2C Marketing Manager
                    Goal: Ask customer feedback to develop 3 personas for personalized marketing and product development.
                    Survey Questions:

                        How would you describe your typical skincare/makeup routine?
                        What factors influence your purchasing decisions when it comes to skincare/makeup products?
                        Can you describe a recent positive/negative experience you've had with a skincare/makeup product?
                        Which social media platforms do you frequently engage with for beauty-related content?
                        What type of content do you find most helpful when researching skincare/makeup products?
                        How do you prefer to discover new skincare/makeup brands or products?
                    
                    Role: Apple Retail Store Manager
                    Goal: Boost employee engagement and satisfaction to increase retention by 10%+ and hence customer satisfaction.
                    Survey Questions:

                        On a scale of 1 to 10, how satisfied are you with your current role at [company name]?
                        What aspects of your job do you find most rewarding?
                        Do you feel adequately supported by your team/management in your role?
                        How would you rate the opportunities for career growth and development within [company name]?
                        Are there any specific challenges or obstacles you face in your day-to-day work?
                        How likely are you to recommend [company name] as an employer to a friend or colleague?


                    """

            },
            {
                "role": "user",
                "content": f"As a {role}, build a survey to help with {goal}. Generate atleast 10 questions."
            }
        ],
        temperature=1,
        max_tokens=5000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    generated_post = response.choices[0].message.content
    return jsonify({'text': generated_post})


if __name__ == '__main__':
    app.run(debug=True,port=6000)

