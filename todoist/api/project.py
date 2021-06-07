from todoist.models import ProjectModel

from . import ICrud


class ProjectApi(ICrud[ProjectModel]):
    pass
