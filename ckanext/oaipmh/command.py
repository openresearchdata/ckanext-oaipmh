from ckan import model
from ckan.logic import get_action, ValidationError

from ckanext.harvest.commands.harvester import Harvester

class OaipmhHarvesterCommand(Harvester):
    """
    OAI-PMH Harvester command
    """
