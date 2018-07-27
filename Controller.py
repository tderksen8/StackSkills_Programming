import web
from CodeWizard.Models.RegisterModel import RegisterModel
from CodeWizard.Models.LoginModel import LoginModel

urls = {
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegister',
    '/login', 'Login',
    '/check-login', 'CheckLogin'
}

render = web.template.render("Views/Templates/", base="MainLayout")
app = web.application(urls, globals())

# Class/Routes


class Home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()


class PostRegister:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel()
        reg_model.insert_user(data)
        return data.first_name


class Login:
    def GET(self):
        return render.Login()


class CheckLogin:
    def POST(self):
        data = web.input()

        login = LoginModel()
        is_correct = login.check_user(data)

        if is_correct:
            return is_correct

        else:
            return "error"


if __name__ == '__main__':
    app.run()
