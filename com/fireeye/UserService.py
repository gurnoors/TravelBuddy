# import User
#
#
# def validate(data):
#     pass
#
#
# # from kuyruk import Kuyruk
# # kuyruk = Kuyruk()
# # @kuyruk.task
# def persist_user(data):
#     if not validate(data):
#         return (False, 'Bad Request')
#
#     print("persisting user: " , data)
#
#     user = User.User(name=data['name'], phone=data['phone'],
#                 start_date=data['start_date'], end_date=data['end_date'])
#     User.db.session.add(user)
#     User.db.session.commit()
#     print ('user persisted: ', user)
#     return (True, user)