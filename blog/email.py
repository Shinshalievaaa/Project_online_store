from django.core.mail import send_mail


def send_test_email(name):
    subject = f'Письмо о блоге {name}'
    message = 'Привет! Поздравляю! Ваш блог набрал 100 просмотров.'
    sender_email = 'shinshalievaaa@gmail.com'  # Должен совпадать с EMAIL_HOST_USER
    recipient_email = 'shinshalievaaa@gmail.com'  # Ваш адрес (или любой другой)

    send_mail(
        subject,
        message,
        sender_email,
        [recipient_email],  # Обратите внимание: это должен быть список (list)
        fail_silently=False,
    )

    return "Письмо успешно отправлено!"
