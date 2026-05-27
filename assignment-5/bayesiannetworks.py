from pgmpy.models import BayesianNetwork

from pgmpy.factors.discrete import TabularCPD

from pgmpy.inference import VariableElimination


model = BayesianNetwork([
    ('Flu', 'Fever'),
    ('Flu', 'Cough')
])


cpd_flu = TabularCPD(
    variable='Flu',
    variable_card=2,
    values=[[0.95], [0.05]]
)


cpd_fever = TabularCPD(
    variable='Fever',
    variable_card=2,

    values=[
        [0.9, 0.2],
        [0.1, 0.8]
    ],

    evidence=['Flu'],
    evidence_card=[2]
)


cpd_cough = TabularCPD(
    variable='Cough',
    variable_card=2,

    values=[
        [0.8, 0.3],
        [0.2, 0.7]
    ],

    evidence=['Flu'],
    evidence_card=[2]
)


model.add_cpds(
    cpd_flu,
    cpd_fever,
    cpd_cough
)


print(model.check_model())


inference = VariableElimination(model)


result = inference.query(

    variables=['Flu'],

    evidence={
        'Fever': 1,
        'Cough': 1
    }
)

print(result)