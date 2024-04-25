import pandas as pd

def min_max_scaling():
   df = pd.read_csv('data2.csv')
   scaled_df = df.copy()
   for col in df.columns[2:]:
      min_val = df[col].min()
      max_val = df[col].max()
      scaled_df[col] = (df[col] - min_val) / (max_val - min_val)
   return scaled_df

# scaled_df = min_max_scaling()


def calculate_score(tech_requirements, user_requirements):
   scores = []
   for col, req in user_requirements.items():
      nearest_value = min(tech_requirements, key=lambda x: abs(x - req))
      scores.append(nearest_value)
   return sum(scores) / len(scores) if scores else 0


def suggest_tech_stack(df, user_requirements):
   recommended_tech = []
   categories = ['Frontend', 'Backend', 'Middleware', 'Database', 'Cybersecurity', 'Cloud Computing', 'IoT']

   for category in categories:
      category_df = df[df['Category'] == category]
      scores = {}
      for idx, row in category_df.iterrows():
            score = calculate_score(row.tolist()[2:], user_requirements)
            scores[row['Technology']] = score

      top_technologies = sorted(scores, key=scores.get, reverse=True)[:2]
      if top_technologies:
            recommended_tech.append(" or ".join(top_technologies))
   return recommended_tech


def get_user_requirements():
   requirements = {}
   print("Please enter your requirements for the tech stack (between 0 and 1):")

   # Developer Experience Required
   while True:
      try:
            dev_exp_input = float(input("Developer Experience Required (0 to 1): "))
            if 0 <= dev_exp_input <= 1:
               requirements['DeveloperExperienceRequired'] = dev_exp_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")

   # Complexity of Project
   while True:
      try:
            complexity_input = float(input("Complexity of Project (0 to 1): "))
            if 0 <= complexity_input <= 1:
               requirements['ComplexityOfProject'] = complexity_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")

   # Project Scale
   while True:
      try:
            scale_input = float(input("Project Scale (0 to 1): "))
            if 0 <= scale_input <= 1:
               requirements['ProjectScale'] = scale_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")

   # Performance of Technology
   while True:
      try:
            performance_input = float(input("Performance of Technology (0 to 1): "))
            if 0 <= performance_input <= 1:
               requirements['PerformanceOfTechnology'] = performance_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")

   # Community Support
   while True:
      try:
            community_input = float(input("Community Support (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['CommunitySupport'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Scalability (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['Scalability'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Security Features (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['SecurityFeatures'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Cost (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['Cost'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Integration Capabilities (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['IntegrationCapabilities'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Documentation Quality (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['DocumentationQuality'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Learning Curve (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['LearningCurve'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Community Adoption (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['CommunityAdoption'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Performance Scaling (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['PerformanceScaling'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Vendor LockIn (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['VendorLockIn'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("Ecosystem Support (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['EcosystemSupport'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   while True:
      try:
            community_input = float(input("LongTerm Support (0 to 1): "))
            if 0 <= community_input <= 1:
               requirements['LongTermSupport'] = community_input
               break
            else:
               print("Invalid input. Please enter a number between 0 and 1.")
      except ValueError:
            print("Invalid input. Please enter a number.")
         
   

   return requirements

# user_requirements = get_user_requirements()

# recommended_tech = suggest_tech_stack(scaled_df, user_requirements)

# if recommended_tech:
#    print("\nRecommended Tech Stack:")
#    for tech in recommended_tech:
#       print(tech)
# else:
#    print("No technologies match all of the specified requirements.")
