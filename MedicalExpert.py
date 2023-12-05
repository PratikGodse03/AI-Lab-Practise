from pyknow import *

# Define the expert system's knowledge base
class MedicalExpert(KnowledgeEngine):
    @Rule(Fact(symptom='fever') & Fact(location='chest') & Fact(duration='several days'))
    def rule_1(self):
        self.declare(Fact(diagnosis='possible flu'))

    @Rule(Fact(symptom='fever') & Fact(location='head') & Fact(duration='less than a day'))
    def rule_2(self):
        self.declare(Fact(diagnosis='possible migraine'))

    @Rule(Fact(symptom='cough') & Fact(location='chest') & Fact(duration='several days'))
    def rule_3(self):
        self.declare(Fact(diagnosis='possible pneumonia'))

    @Rule(Fact(symptom='cough') & Fact(location='head') & Fact(duration='less than a day'))
    def rule_4(self):
        self.declare(Fact(diagnosis='possible common cold'))

# Create an instance of the medical expert system
expert_system = MedicalExpert()

# Provide symptoms as facts to the system
expert_system.reset()
expert_system.declare(Fact(symptom='fever'))
expert_system.declare(Fact(location='chest'))
expert_system.declare(Fact(duration='several days'))

# Run the expert system
expert_system.run()

# Retrieve the diagnosis from the system
diagnosis = expert_system.facts.get(Fact(diagnosis=lambda x: True))
if diagnosis:
    print("The possible diagnosis is:", diagnosis[0].fields['diagnosis'])
else:
    print("No specific diagnosis could be made based on the provided symptoms.")

