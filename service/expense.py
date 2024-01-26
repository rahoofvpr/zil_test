
class Expense():
    @staticmethod
    def create_expense(ins_expense,db = None):
        # import pdb;pdb.set_trace()
        db.add(instance = ins_expense)
        db.commit()
        db.refresh(ins_expense)
        return ins_expense