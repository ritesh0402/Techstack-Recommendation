import pandas as pd

df = pd.read_csv('data.csv')

DEVELOPER_EXP_MAP = {1: 'Low', 2: 'Moderate', 3: 'High'}
PROJECT_COMPLEXITY_MAP = {1: 'Small', 2: 'Medium', 3: 'Large'}
PROJECT_SCALE_MAP = {1: 'Small', 2: 'Medium', 3: 'Large'}
PERFORMANCE_MAP = {1: 'Moderate', 2: 'High'}
COMMUNITY_SUPPORT_MAP = {1: 'Low', 2: 'High'}


def calculate_score(tech_requirements, user_requirements):
   score = 0
   for col, req in user_requirements.items():
      if tech_requirements[col].lower() == req.lower():
            score += 1
   return score


def suggest_tech_stack(df, user_requirements):
   recommended_tech = []
   categories = ['Frontend', 'Backend', 'Middleware', 'Database', 'Cybersecurity']

   for category in categories:
      # print(f"\nCategory: {category}")
      category_df = df[df['Catagory'] == category]  # Corrected column name 'Category'
      scores = {}
      for idx, row in category_df.iterrows():
            score = calculate_score(row, user_requirements)
            # print(f"Technology: {row['Technology']}, Score: {score}")
            scores[row['Technology']] = score

      # Sort technologies by score and get top two
      top_technologies = sorted(scores, key=scores.get, reverse=True)[:2]
      if top_technologies:
            recommended_tech.append(" or ".join(top_technologies))

   return recommended_tech



def get_user_requirements():
   requirements = {}
   print("Please enter your requirements for the tech stack:")

   # Developer Experience Required
   while True:
      try:
            dev_exp_input = int(input("Developer Experience Required (1: Low, 2: Moderate, 3: High): "))
            if dev_exp_input in DEVELOPER_EXP_MAP:
               requirements['Developer Experience Required'] = DEVELOPER_EXP_MAP[dev_exp_input]
               break
            else:
               print("Invalid input. Please enter a number between 1 and 4.")
      except ValueError:
            print("Invalid input. Please enter a number.")

   # Complexity of Project
   while True:
      try:
            complexity_input = int(input("Complexity of Project (1: Small, 2: Medium, 3: Large): "))
            if complexity_input in PROJECT_COMPLEXITY_MAP:
               requirements['Complexity of Project'] = PROJECT_COMPLEXITY_MAP[complexity_input]
               break
            else:
               print("Invalid input. Please enter a number between 1 and 3.")
      except ValueError:
            print("Invalid input. Please enter a number.")

   # Project Scale
   while True:
      try:
            scale_input = int(input("Project Scale (1: Small, 2: Medium, 3: Large): "))
            if scale_input in PROJECT_SCALE_MAP:
               requirements['Project Scale'] = PROJECT_SCALE_MAP[scale_input]
               break
            else:
               print("Invalid input. Please enter a number between 1 and 3.")
      except ValueError:
            print("Invalid input. Please enter a number.")

   # Performance of Technology
   while True:
      try:
            performance_input = int(input("Performance of Technology (1: Moderate, 2: High): "))
            if performance_input in PERFORMANCE_MAP:
               requirements['Performance of Technology'] = PERFORMANCE_MAP[performance_input]
               break
            else:
               print("Invalid input. Please enter either 1 or 2.")
      except ValueError:
            print("Invalid input. Please enter a number.")

   # Community Support
   while True:
      try:
            community_input = int(input("Community Support (1: Low, 2: High): "))
            if community_input in COMMUNITY_SUPPORT_MAP:
               requirements['Community Support'] = COMMUNITY_SUPPORT_MAP[community_input]
               break
            else:
               print("Invalid input. Please enter either 1 or 2.")
      except ValueError:
            print("Invalid input. Please enter a number.")

   return requirements




user_requirements = get_user_requirements()
recommended_tech = suggest_tech_stack(df, user_requirements)

if recommended_tech:
   print("\n\nRecommended Tech Stack:")
   for tech in recommended_tech:
      print(tech)
else:
   print("No technologies match all of the specified requirements.")