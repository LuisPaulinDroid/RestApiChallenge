from project import app

# Setting production configuration for application
app.config.from_object('config.BaseConfig')

if __name__ == '__main__':
    app.run(host='0.0.0.0')