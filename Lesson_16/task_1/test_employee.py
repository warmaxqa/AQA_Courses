from Lesson_16.task_1.employee import TeamLead
from assertpy import assert_that


class TestEmployee:

    qa_automation_team_lead: TeamLead = TeamLead("Max", salary=5000, department="Test Python QA Engineer", team_size=5)

    expected_max_attrs: dict[str, object] = {
        "name": "Max",
        "salary": 5000,
        "department": "Test Python QA Engineer",
        "team_size": 5
    }

    expected_failed_max_attrs: dict[str, object] = {
        "name": "Max",
        "salary": 5000,
        "department": "Test Python QA Engineer",
        "team_size": 6
    }

    def test_employee_attrs(self):
        assert_that(self.qa_automation_team_lead.__dict__,
                    description="Desired user attrs are not equal to desire dict of attributes") \
            .is_equal_to(self.expected_max_attrs)

    def test_employee_negative_attrs_values(self):
        assert_that(self.qa_automation_team_lead.__dict__,
                    description="Desired user attrs are not equal to desire dict of attributes") \
            .is_equal_to(self.expected_failed_max_attrs)
