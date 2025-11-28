from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home

class HospitalHome(Home):
    @http.route('/web', type='http', auth="user", website=True)
    def web_client(self, s_action=None, **kw):
        return super(HospitalHome, self).web_client(s_action, **kw)

class HospitalWebsite(http.Controller):

    @http.route('/hospital', auth='public', website=True)
    def hospital_home(self, **kw):
        return request.render('hospital_management.hospital_home_template')

    @http.route('/hospital/about', auth='public', website=True)
    def hospital_about(self, **kw):
        return request.render('hospital_management.hospital_about_template')

    @http.route('/hospital/services', auth='public', website=True)
    def hospital_services(self, **kw):
        return request.render('hospital_management.hospital_services_template')

    @http.route('/hospital/contacts', auth='public', website=True)
    def hospital_contacts(self, **kw):
        return request.render('hospital_management.hospital_contacts_template')

    @http.route('/hospital/blogs', auth='public', website=True)
    def hospital_blogs(self, **kw):
        return request.render('hospital_management.hospital_blogs_template')

    @http.route('/hospital/news', auth='public', website=True)
    def hospital_news(self, **kw):
        return request.render('hospital_management.hospital_news_template')

    @http.route('/hospital/dashboard/doctor', auth='user', website=True)
    def doctor_dashboard(self, **kw):
        if not request.env.user.has_group('hospital_management.group_hospital_doctor'):
            return request.redirect('/web/login')
        return request.render('hospital_management.doctor_dashboard_template')

    @http.route('/hospital/dashboard/patient', auth='user', website=True)
    def patient_dashboard(self, **kw):
        if not request.env.user.has_group('hospital_management.group_hospital_patient'):
            return request.redirect('/web/login')
        return request.render('hospital_management.patient_dashboard_template')

    @http.route('/hospital/dashboard/admin', auth='user', website=True)
    def admin_dashboard(self, **kw):
        if not request.env.user.has_group('hospital_management.group_hospital_admin'):
            return request.redirect('/web/login')
        return request.render('hospital_management.admin_dashboard_template')

    @http.route('/hospital/management', auth='user', website=True)
    def hospital_management(self, **kw):
        if request.env.user._is_public():
            return request.redirect('/web/login')
        menu = request.env.ref('hospital_management.menu_hospital_root')
        return request.redirect('/web#menu_id=%s' % menu.id)