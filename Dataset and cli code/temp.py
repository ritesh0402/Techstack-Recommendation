import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Read the data from CSV
df = pd.read_csv('data2.csv')

# Function to perform min-max scaling on the dataframe
def min_max_scaling(df):
   scaled_df = df.copy()
   for col in df.columns[2:]:
      min_val = df[col].min()
      max_val = df[col].max()
      scaled_df[col] = (df[col] - min_val) / (max_val - min_val)
   return scaled_df

# Perform min-max scaling on the dataframe
scaled_df = min_max_scaling(df)

# Function to calculate score using fuzzy logic
def calculate_score_fuzzy(*args):
   # Define antecedents
   dev_exp = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Developer Experience Required')
   complexity = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Complexity of Project')
   project_scale = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Project Scale')
   performance = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Performance of Technology')
   community = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Community Support')
   scalability = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Scalability')
   security = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Security Features')
   cost = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Cost')
   integration = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Integration Capabilities')
   documentation = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Documentation Quality')
   learning = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Learning Curve')
   adoption = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Community Adoption')
   scaling = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Performance Scaling')
   lock_in = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Vendor LockIn')
   ecosystem = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Ecosystem Support')
   support = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'LongTerm Support')
   score = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'Score')

      # Define membership functions for all antecedents
   dev_exp = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Developer Experience Required')
   dev_exp['low'] = fuzz.trimf(dev_exp.universe, [0, 0, 0.5])
   dev_exp['medium'] = fuzz.trimf(dev_exp.universe, [0, 0.5, 1])
   dev_exp['high'] = fuzz.trimf(dev_exp.universe, [0.5, 1, 1])

   complexity = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Complexity of Project')
   complexity['low'] = fuzz.trimf(complexity.universe, [0, 0, 0.5])
   complexity['medium'] = fuzz.trimf(complexity.universe, [0, 0.5, 1])
   complexity['high'] = fuzz.trimf(complexity.universe, [0.5, 1, 1])

   project_scale = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Project Scale')
   project_scale['low'] = fuzz.trimf(project_scale.universe, [0, 0, 0.5])
   project_scale['medium'] = fuzz.trimf(project_scale.universe, [0, 0.5, 1])
   project_scale['high'] = fuzz.trimf(project_scale.universe, [0.5, 1, 1])

   performance = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Performance of Technology')
   performance['low'] = fuzz.trimf(performance.universe, [0, 0, 0.5])
   performance['medium'] = fuzz.trimf(performance.universe, [0, 0.5, 1])
   performance['high'] = fuzz.trimf(performance.universe, [0.5, 1, 1])

   community = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Community Support')
   community['low'] = fuzz.trimf(community.universe, [0, 0, 0.5])
   community['medium'] = fuzz.trimf(community.universe, [0, 0.5, 1])
   community['high'] = fuzz.trimf(community.universe, [0.5, 1, 1])

   scalability = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Scalability')
   scalability['low'] = fuzz.trimf(scalability.universe, [0, 0, 0.5])
   scalability['medium'] = fuzz.trimf(scalability.universe, [0, 0.5, 1])
   scalability['high'] = fuzz.trimf(scalability.universe, [0.5, 1, 1])

   security = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Security Features')
   security['low'] = fuzz.trimf(security.universe, [0, 0, 0.5])
   security['medium'] = fuzz.trimf(security.universe, [0, 0.5, 1])
   security['high'] = fuzz.trimf(security.universe, [0.5, 1, 1])

   cost = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Cost')
   cost['low'] = fuzz.trimf(cost.universe, [0, 0, 0.5])
   cost['medium'] = fuzz.trimf(cost.universe, [0, 0.5, 1])
   cost['high'] = fuzz.trimf(cost.universe, [0.5, 1, 1])

   integration = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Integration Capabilities')
   integration['low'] = fuzz.trimf(integration.universe, [0, 0, 0.5])
   integration['medium'] = fuzz.trimf(integration.universe, [0, 0.5, 1])
   integration['high'] = fuzz.trimf(integration.universe, [0.5, 1, 1])

   documentation = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Documentation Quality')
   documentation['low'] = fuzz.trimf(documentation.universe, [0, 0, 0.5])
   documentation['medium'] = fuzz.trimf(documentation.universe, [0, 0.5, 1])
   documentation['high'] = fuzz.trimf(documentation.universe, [0.5, 1, 1])

   learning = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Learning Curve')
   learning['low'] = fuzz.trimf(learning.universe, [0, 0, 0.5])
   learning['medium'] = fuzz.trimf(learning.universe, [0, 0.5, 1])
   learning['high'] = fuzz.trimf(learning.universe, [0.5, 1, 1])

   adoption = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Community Adoption')
   adoption['low'] = fuzz.trimf(adoption.universe, [0, 0, 0.5])
   adoption['medium'] = fuzz.trimf(adoption.universe, [0, 0.5, 1])
   adoption['high'] = fuzz.trimf(adoption.universe, [0.5, 1, 1])

   scaling = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Performance Scaling')
   scaling['low'] = fuzz.trimf(scaling.universe, [0, 0, 0.5])
   scaling['medium'] = fuzz.trimf(scaling.universe, [0, 0.5, 1])
   scaling['high'] = fuzz.trimf(scaling.universe, [0.5, 1, 1])

   lock_in = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Vendor LockIn')
   lock_in['low'] = fuzz.trimf(lock_in.universe, [0, 0, 0.5])
   lock_in['medium'] = fuzz.trimf(lock_in.universe, [0, 0.5, 1])
   lock_in['high'] = fuzz.trimf(lock_in.universe, [0.5, 1, 1])

   ecosystem = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Ecosystem Support')
   ecosystem['low'] = fuzz.trimf(ecosystem.universe, [0, 0, 0.5])
   ecosystem['medium'] = fuzz.trimf(ecosystem.universe, [0, 0.5, 1])
   ecosystem['high'] = fuzz.trimf(ecosystem.universe, [0.5, 1, 1])

   support = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'LongTerm Support')
   support['low'] = fuzz.trimf(support.universe, [0, 0, 0.5])
   support['medium'] = fuzz.trimf(support.universe, [0, 0.5, 1])
   support['high'] = fuzz.trimf(support.universe, [0.5, 1, 1])

   # Define rules
   rule1 = ctrl.Rule(dev_exp['low'] & complexity['low'] & project_scale['low'] & performance['low'] &
                     community['low'] & scalability['low'] & security['low'] & cost['low'] &
                     integration['low'] & documentation['low'] & learning['low'] & adoption['low'] &
                     scaling['low'] & lock_in['low'] & ecosystem['low'] & support['low'], score['low'])
   rule2 = ctrl.Rule(dev_exp['medium'] & complexity['medium'] & project_scale['medium'] & performance['medium'] &
                     community['medium'] & scalability['medium'] & security['medium'] & cost['medium'] &
                     integration['medium'] & documentation['medium'] & learning['medium'] & adoption['medium'] &
                     scaling['medium'] & lock_in['medium'] & ecosystem['medium'] & support['medium'], score['medium'])
   rule3 = ctrl.Rule(dev_exp['high'] & complexity['high'] & project_scale['high'] & performance['high'] &
                     community['high'] & scalability['high'] & security['high'] & cost['high'] &
                     integration['high'] & documentation['high'] & learning['high'] & adoption['high'] &
                     scaling['high'] & lock_in['high'] & ecosystem['high'] & support['high'], score['high'])

   # Combine rules into a control system
   tech_stack_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

   # Create a control system simulation
   tech_stack_sim = ctrl.ControlSystemSimulation(tech_stack_ctrl)

   # Use the control system to compute output
   tech_stack_sim.input['Developer Experience Required'] = args[0]
   tech_stack_sim.input['Complexity of Project'] = args[1]
   tech_stack_sim.input['Project Scale'] = args[2]
   tech_stack_sim.input['Performance of Technology'] = args[3]
   tech_stack_sim.input['Community Support'] = args[4]
   tech_stack_sim.input['Scalability'] = args[5]
   tech_stack_sim.input['Security Features'] = args[6]
   tech_stack_sim.input['Cost'] = args[7]
   tech_stack_sim.input['Integration Capabilities'] = args[8]
   tech_stack_sim.input['Documentation Quality'] = args[9]
   tech_stack_sim.input['Learning Curve'] = args[10]
   tech_stack_sim.input['Community Adoption'] = args[11]
   tech_stack_sim.input['Performance Scaling'] = args[12]
   tech_stack_sim.input['Vendor LockIn'] = args[13]
   tech_stack_sim.input['Ecosystem Support'] = args[14]
   tech_stack_sim.input['LongTerm Support'] = args[15]

   tech_stack_sim.compute()

   # Return the output value
   return tech_stack_sim.output['Score']


# Function to suggest tech stack based on user requirements using fuzzy logic
def suggest_tech_stack_fuzzy(df, user_requirements):
   recommended_tech = []
   categories = ['Frontend', 'Backend', 'Middleware', 'Database', 'Cybersecurity', 'Cloud Computing', 'IoT']

   for category in categories:
      category_df = df[df['Category'] == category]
      scores = {}
      for idx, row in category_df.iterrows():
            score = calculate_score_fuzzy(
               row['DeveloperExperienceRequired'], row['ComplexityOfProject'], row['ProjectScale'],
               row['PerformanceOfTechnology'], row['CommunitySupport'], row['Scalability'], 
               row['SecurityFeatures'], row['Cost'], row['IntegrationCapabilities'], 
               row['DocumentationQuality'], row['LearningCurve'], row['CommunityAdoption'], 
               row['PerformanceScaling'], row['VendorLockIn'], row['EcosystemSupport'], 
               row['LongTermSupport'], **user_requirements)
            scores[row['Technology']] = score

      top_technologies = sorted(scores, key=scores.get, reverse=True)[:2]
      if top_technologies:
            recommended_tech.append(" or ".join(top_technologies))
   return recommended_tech

# Function to get user requirements from the user
def get_user_requirements():
   requirements = {}
   print("Please enter your requirements for the tech stack (between 0 and 1):")
   # Get user inputs for all requirements
   return requirements

# Get user requirements
user_requirements = get_user_requirements()

# Suggest tech stack based on user requirements
recommended_tech = suggest_tech_stack_fuzzy(scaled_df, user_requirements)

if recommended_tech:
    print("\nRecommended Tech Stack:")
    for tech in recommended_tech:
        print(tech)
else:
    print("No technologies match all of the specified requirements.")
