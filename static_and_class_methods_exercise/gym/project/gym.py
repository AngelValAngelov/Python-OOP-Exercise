from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def add_obj(list_obj, obj):
        if obj not in list_obj:
            list_obj.append(obj)

    def add_customer(self, customer: Customer):
        Gym.add_obj(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        Gym.add_obj(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        Gym.add_obj(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        Gym.add_obj(self.plans, plan)

    def add_subscription(self, subscription: Subscription):
        Gym.add_obj(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):
        subscription = '\n'.join([s.__repr__() for s in self.subscriptions if s.id == subscription_id]) + '\n'
        customer = '\n'.join([c.__repr__() for c in self.customers if c.id == subscription_id]) + '\n'
        trainer = '\n'.join([t.__repr__() for t in self.trainers if t.id == subscription_id]) + '\n'
        equipment = '\n'.join([e.__repr__() for e in self.equipment if e.id == subscription_id]) + '\n'
        plan = '\n'.join([p.__repr__() for p in self.plans if p.id == subscription_id]) + '\n'
        return subscription + customer + trainer + equipment + plan


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
