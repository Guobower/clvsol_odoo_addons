# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import api, fields, models


class PersonHistoryLog(models.Model):
    _description = 'Person History Log'
    _name = 'clv.person.history.log'
    _inherit = 'clv.object.log'

    person_history_id = fields.Many2one(
        comodel_name='clv.person.history',
        string='Person History',
        required=True,
        ondelete='cascade'
    )


class PersonHistory(models.Model):
    _name = "clv.person.history"
    _inherit = 'clv.person.history', 'clv.log.model'

    log_ids = fields.One2many(
        comodel_name='clv.person.history.log',
        inverse_name='person_history_id',
        string='Person History Log',
        readonly=True
    )

    @api.one
    def insert_object_log(self, person_history_id, values, action, notes):
        if self.active_log or 'active_log' in values:
            if str(values).find("'category_ids': clv.person.history.category(") == -1:
                vals = {
                    'person_history_id': person_history_id,
                    'values': values,
                    'action': action,
                    'notes': notes,
                }
                self.env['clv.person.history.log'].create(vals)
