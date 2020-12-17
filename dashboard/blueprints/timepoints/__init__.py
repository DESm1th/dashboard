from flask import Blueprint

time_bp = Blueprint(
    'timepoints',
    __name__,
    template_folder='templates',
    url_prefix='/study/<string:study_id>/timepoint/<string:timepoint_id>'
)

ajax_bp = Blueprint(
    'ajax_timepoints',
    __name__,
    template_folder='templates',
    url_prefix='/timepoint'
)

from . import views
