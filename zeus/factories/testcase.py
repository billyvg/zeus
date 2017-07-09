import factory
import factory.fuzzy

from faker import Factory
faker = Factory.create()

from zeus import models
from zeus.constants import Result

from .types import GUIDFactory


class TestCaseFactory(factory.Factory):
    id = GUIDFactory()
    name = factory.LazyAttribute(
        lambda o: 'tests.%s.%s.%s' % (faker.word(), faker.word(), faker.word())
    )
    job = factory.SubFactory('zeus.factories.JobFactory')
    job_id = factory.SelfAttribute('job.id')
    repository = factory.SelfAttribute('job.repository')
    repository_id = factory.SelfAttribute('job.repository_id')
    result = Result.passed
    duration = factory.Faker('random_int', min=1, max=100000)
    date_created = factory.Faker('date_time')

    class Meta:
        model = models.TestCase
