from flask import Blueprint,render_template, redirect, url_for, flash,session,request,current_app
from flask_login import login_user,logout_user,login_required
from jobplus.models import User,Company,Message
from jobplus.forms import EmessageForm,MessageForm,AdduserForm,AddcompanyForm
from jobplus.decorators import euser_requeired,user_requeired,admin_requeired,login_timeat

company = Blueprint('company', __name__,url_prefix='/company')


@company.route('/')
@login_timeat
def index():
    page = request.args.get('page',default=1,type=int)
    pagination = Company.query.paginate(
        page=page,
        per_page=current_app.config['COMPANY_PER_PAGE'],
        error_out=False
    )
    print(pagination.items)
    return render_template('company/company.html',pagination=pagination)



@company.route('/<int:company_id>')
@login_timeat
def company_des(company_id):
    companys=Company.query.filter_by(id=company_id).first()

    return render_template('company/company_des.html',companys=companys)

