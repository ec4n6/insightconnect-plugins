import komand
import github
from .schema import CloseIssueInput, CloseIssueOutput



class CloseIssue(komand.Action):
  def __init__(self):
      super(self.__class__, self).__init__(
              name='close_issue',
              description='Closes an Issue',
              input=CloseIssueInput(),
              output=CloseIssueOutput())


  def run(self, params={}):
    if params.get('organization') and params.get('repository'):
      g = self.connection.github_user
      issue = g.get_organization(params.get('organization')).get_repo(params.get('repository')).get_issue(int(params.get('issue_number')))
    else:
      g = self.connection.user
      issue = g.get_repo(params.get('repository')).get_issue(int(params.get('issue_number')))

    issue_params = {"state": "closed"}

    issue = issue.edit(**issue_params)

    return {'url': issue.html_url}
