from tkinter import *
import tkinter.font as font
import sqlite3

root = Tk()
root.title('MCQ')
root.resizable(0, 0)

score = 0

conn = sqlite3.connect("MCQDB")
c = conn.cursor()

'''
c.execute("""CREATE TABLE MCQDB(
            Question text,
            option1 text,
            option2 text,
            option3 text,
            option4 text,
            crtoption integer)
            """)
'''


def chgquestions():
    def update(q, a1, b2, c3, d4, co, id):
        conn = sqlite3.connect("MCQDB")
        c = conn.cursor()

        c.execute("""UPDATE MCQDB SET
                    Question=:q,
                    option1=:a,
                    option2=:b,
                    option3=:c,
                    option4=:d,
                    crtoption=:co
                    WHERE oid=:id""",
                  {
                      'q': q,
                      'a': a1,
                      'b': b2,
                      'c': c3,
                      'd': d4,
                      'co': co,
                      'id': id
                  })

        conn.commit()
        conn.close()

    def chgquestionfive():
        global Qno_4
        global question_4
        global option1_4
        global option2_4
        global option3_4
        global option4_4
        global crtoption_4
        global question_entry_4
        global option1_entry_4
        global option2_entry_4
        global option3_entry_4
        global option4_entry_4
        global crtoption_entry_4
        global save_button_4
        global next_button_4

        Qno_4.grid_forget()
        question_4.grid_forget()
        option1_4.grid_forget()
        option2_4.grid_forget()
        option3_4.grid_forget()
        option4_4.grid_forget()
        crtoption_4.grid_forget()
        question_entry_4.grid_forget()
        option1_entry_4.grid_forget()
        option2_entry_4.grid_forget()
        option3_entry_4.grid_forget()
        option4_entry_4.grid_forget()
        crtoption_entry_4.grid_forget()
        save_button_4.grid_forget()
        next_button_4.grid_forget()

        global Qno_5
        global question_5
        global option1_5
        global option2_5
        global option3_5
        global option4_5
        global crtoption_5
        global question_entry_5
        global option1_entry_5
        global option2_entry_5
        global option3_entry_5
        global option4_entry_5
        global crtoption_entry_5
        global save_button_5
        global next_button_5

        conn = sqlite3.connect("MCQDB")
        c = conn.cursor()

        Qno_5 = Label(editor, text="Question Number 5 - ")
        Qno_5.grid(row=0, column=0)

        question_5 = Label(editor, text="Question :")
        question_5.grid(row=1, column=0)

        option1_5 = Label(editor, text="Option 1 :")
        option1_5.grid(row=2, column=0)

        option2_5 = Label(editor, text="Option 2 :")
        option2_5.grid(row=3, column=0)

        option3_5 = Label(editor, text="Option 3 :")
        option3_5.grid(row=4, column=0)

        option4_5 = Label(editor, text="Option 4 :")
        option4_5.grid(row=5, column=0)

        crtoption_5 = Label(editor, text="Correct Option :")
        crtoption_5.grid(row=6, column=0)

        question_entry_5 = Entry(editor, width=30)
        question_entry_5.grid(row=1, column=1)

        option1_entry_5 = Entry(editor, width=30)
        option1_entry_5.grid(row=2, column=1)

        option2_entry_5 = Entry(editor, width=30)
        option2_entry_5.grid(row=3, column=1)

        option3_entry_5 = Entry(editor, width=30)
        option3_entry_5.grid(row=4, column=1)

        option4_entry_5 = Entry(editor, width=30)
        option4_entry_5.grid(row=5, column=1)

        crtoption_entry_5 = Entry(editor, width=30)
        crtoption_entry_5.grid(row=6, column=1)

        c.execute("SELECT * FROM MCQDB WHERE oid=" + str(5))
        A = c.fetchall()

        question_entry_5.insert(0, A[0][0])
        option1_entry_5.insert(0, A[0][1])
        option2_entry_5.insert(0, A[0][2])
        option3_entry_5.insert(0, A[0][3])
        option4_entry_5.insert(0, A[0][4])
        crtoption_entry_5.insert(0, A[0][5])

        save_button_5 = Button(editor, text="Save",
                               command=lambda: update(question_entry_5.get(), option1_entry_5.get(),
                                                      option2_entry_5.get(), option3_entry_5.get(),
                                                      option4_entry_5.get(), crtoption_entry_5.get(), 5))
        save_button_5.grid(row=7, column=0, sticky=W)

        next_button_5 = Button(editor, text="Exit", command=editor.quit)
        next_button_5.grid(row=7, column=1, sticky=E)

        conn.commit()
        conn.close()

    def chgquestionfour():
        global Qno_3
        global question_3
        global option1_3
        global option2_3
        global option3_3
        global option4_3
        global crtoption_3
        global question_entry_3
        global option1_entry_3
        global option2_entry_3
        global option3_entry_3
        global option4_entry_3
        global crtoption_entry_3
        global save_button_3
        global next_button_3

        Qno_3.grid_forget()
        question_3.grid_forget()
        option1_3.grid_forget()
        option2_3.grid_forget()
        option3_3.grid_forget()
        option4_3.grid_forget()
        crtoption_3.grid_forget()
        question_entry_3.grid_forget()
        option1_entry_3.grid_forget()
        option2_entry_3.grid_forget()
        option3_entry_3.grid_forget()
        option4_entry_3.grid_forget()
        crtoption_entry_3.grid_forget()
        save_button_3.grid_forget()
        next_button_3.grid_forget()

        global Qno_4
        global question_4
        global option1_4
        global option2_4
        global option3_4
        global option4_4
        global crtoption_4
        global question_entry_4
        global option1_entry_4
        global option2_entry_4
        global option3_entry_4
        global option4_entry_4
        global crtoption_entry_4
        global save_button_4
        global next_button_4

        conn = sqlite3.connect("MCQDB")
        c = conn.cursor()

        Qno_4 = Label(editor, text="Question Number 4 - ")
        Qno_4.grid(row=0, column=0)

        question_4 = Label(editor, text="Question :")
        question_4.grid(row=1, column=0)

        option1_4 = Label(editor, text="Option 1 :")
        option1_4.grid(row=2, column=0)

        option2_4 = Label(editor, text="Option 2 :")
        option2_4.grid(row=3, column=0)

        option3_4 = Label(editor, text="Option 3 :")
        option3_4.grid(row=4, column=0)

        option4_4 = Label(editor, text="Option 4 :")
        option4_4.grid(row=5, column=0)

        crtoption_4 = Label(editor, text="Correct Option :")
        crtoption_4.grid(row=6, column=0)

        question_entry_4 = Entry(editor, width=30)
        question_entry_4.grid(row=1, column=1)

        option1_entry_4 = Entry(editor, width=30)
        option1_entry_4.grid(row=2, column=1)

        option2_entry_4 = Entry(editor, width=30)
        option2_entry_4.grid(row=3, column=1)

        option3_entry_4 = Entry(editor, width=30)
        option3_entry_4.grid(row=4, column=1)

        option4_entry_4 = Entry(editor, width=30)
        option4_entry_4.grid(row=5, column=1)

        crtoption_entry_4 = Entry(editor, width=30)
        crtoption_entry_4.grid(row=6, column=1)

        c.execute("SELECT * FROM MCQDB WHERE oid=" + str(4))
        A = c.fetchall()

        question_entry_4.insert(0, A[0][0])
        option1_entry_4.insert(0, A[0][1])
        option2_entry_4.insert(0, A[0][2])
        option3_entry_4.insert(0, A[0][3])
        option4_entry_4.insert(0, A[0][4])
        crtoption_entry_4.insert(0, A[0][5])

        save_button_4 = Button(editor, text="Save",
                               command=lambda: update(question_entry_4.get(), option1_entry_4.get(),
                                                      option2_entry_4.get(), option3_entry_4.get(),
                                                      option4_entry_4.get(), crtoption_entry_4.get(), 4))
        save_button_4.grid(row=7, column=0, sticky=W)

        next_button_4 = Button(editor, text=">>", command=chgquestionfive)
        next_button_4.grid(row=7, column=1, sticky=E)

        conn.commit()
        conn.close()

    def chgquestionthree():
        global Qno_2
        global question_2
        global option1_2
        global option2_2
        global option3_2
        global option4_2
        global crtoption_2
        global question_entry_2
        global option1_entry_2
        global option2_entry_2
        global option3_entry_2
        global option4_entry_2
        global crtoption_entry_2
        global save_button_2
        global next_button_2

        Qno_2.grid_forget()
        question_2.grid_forget()
        option1_2.grid_forget()
        option2_2.grid_forget()
        option3_2.grid_forget()
        option4_2.grid_forget()
        crtoption_2.grid_forget()
        question_entry_2.grid_forget()
        option1_entry_2.grid_forget()
        option2_entry_2.grid_forget()
        option3_entry_2.grid_forget()
        option4_entry_2.grid_forget()
        crtoption_entry_2.grid_forget()
        save_button_2.grid_forget()
        next_button_2.grid_forget()

        global Qno_3
        global question_3
        global option1_3
        global option2_3
        global option3_3
        global option4_3
        global crtoption_3
        global question_entry_3
        global option1_entry_3
        global option2_entry_3
        global option3_entry_3
        global option4_entry_3
        global crtoption_entry_3
        global save_button_3
        global next_button_3

        conn = sqlite3.connect("MCQDB")
        c = conn.cursor()

        Qno_3 = Label(editor, text="Question Number 3 - ")
        Qno_3.grid(row=0, column=0)

        question_3 = Label(editor, text="Question :")
        question_3.grid(row=1, column=0)

        option1_3 = Label(editor, text="Option 1 :")
        option1_3.grid(row=2, column=0)

        option2_3 = Label(editor, text="Option 2 :")
        option2_3.grid(row=3, column=0)

        option3_3 = Label(editor, text="Option 3 :")
        option3_3.grid(row=4, column=0)

        option4_3 = Label(editor, text="Option 4 :")
        option4_3.grid(row=5, column=0)

        crtoption_3 = Label(editor, text="Correct Option :")
        crtoption_3.grid(row=6, column=0)

        question_entry_3 = Entry(editor, width=30)
        question_entry_3.grid(row=1, column=1)

        option1_entry_3 = Entry(editor, width=30)
        option1_entry_3.grid(row=2, column=1)

        option2_entry_3 = Entry(editor, width=30)
        option2_entry_3.grid(row=3, column=1)

        option3_entry_3 = Entry(editor, width=30)
        option3_entry_3.grid(row=4, column=1)

        option4_entry_3 = Entry(editor, width=30)
        option4_entry_3.grid(row=5, column=1)

        crtoption_entry_3 = Entry(editor, width=30)
        crtoption_entry_3.grid(row=6, column=1)

        c.execute("SELECT * FROM MCQDB WHERE oid=" + str(3))
        A = c.fetchall()

        question_entry_3.insert(0, A[0][0])
        option1_entry_3.insert(0, A[0][1])
        option2_entry_3.insert(0, A[0][2])
        option3_entry_3.insert(0, A[0][3])
        option4_entry_3.insert(0, A[0][4])
        crtoption_entry_3.insert(0, A[0][5])

        save_button_3 = Button(editor, text="Save",
                               command=lambda: update(question_entry_3.get(), option1_entry_3.get(),
                                                      option2_entry_3.get(), option3_entry_3.get(),
                                                      option4_entry_3.get(), crtoption_entry_3.get(), 3))
        save_button_3.grid(row=7, column=0, sticky=W)

        next_button_3 = Button(editor, text=">>", command=chgquestionfour)
        next_button_3.grid(row=7, column=1, sticky=E)

        conn.commit()
        conn.close()

    def chgquestiontwo():
        global Qno_1
        global question_1
        global option1_1
        global option2_1
        global option3_1
        global option4_1
        global crtoption_1
        global question_entry_1
        global option1_entry_1
        global option2_entry_1
        global option3_entry_1
        global option4_entry_1
        global crtoption_entry_1
        global save_button_1
        global next_button_1

        Qno_1.grid_forget()
        question_1.grid_forget()
        option1_1.grid_forget()
        option2_1.grid_forget()
        option3_1.grid_forget()
        option4_1.grid_forget()
        crtoption_1.grid_forget()
        question_entry_1.grid_forget()
        option1_entry_1.grid_forget()
        option2_entry_1.grid_forget()
        option3_entry_1.grid_forget()
        option4_entry_1.grid_forget()
        crtoption_entry_1.grid_forget()
        save_button_1.grid_forget()
        next_button_1.grid_forget()

        global Qno_2
        global question_2
        global option1_2
        global option2_2
        global option3_2
        global option4_2
        global crtoption_2
        global question_entry_2
        global option1_entry_2
        global option2_entry_2
        global option3_entry_2
        global option4_entry_2
        global crtoption_entry_2
        global save_button_2
        global next_button_2

        conn = sqlite3.connect("MCQDB")
        c = conn.cursor()

        Qno_2 = Label(editor, text="Question Number 2 - ")
        Qno_2.grid(row=0, column=0)

        question_2 = Label(editor, text="Question :")
        question_2.grid(row=1, column=0)

        option1_2 = Label(editor, text="Option 1 :")
        option1_2.grid(row=2, column=0)

        option2_2 = Label(editor, text="Option 2 :")
        option2_2.grid(row=3, column=0)

        option3_2 = Label(editor, text="Option 3 :")
        option3_2.grid(row=4, column=0)

        option4_2 = Label(editor, text="Option 4 :")
        option4_2.grid(row=5, column=0)

        crtoption_2 = Label(editor, text="Correct Option :")
        crtoption_2.grid(row=6, column=0)

        question_entry_2 = Entry(editor, width=30)
        question_entry_2.grid(row=1, column=1)

        option1_entry_2 = Entry(editor, width=30)
        option1_entry_2.grid(row=2, column=1)

        option2_entry_2 = Entry(editor, width=30)
        option2_entry_2.grid(row=3, column=1)

        option3_entry_2 = Entry(editor, width=30)
        option3_entry_2.grid(row=4, column=1)

        option4_entry_2 = Entry(editor, width=30)
        option4_entry_2.grid(row=5, column=1)

        crtoption_entry_2 = Entry(editor, width=30)
        crtoption_entry_2.grid(row=6, column=1)

        c.execute("SELECT * FROM MCQDB WHERE oid=" + str(2))
        A = c.fetchall()

        question_entry_2.insert(0, A[0][0])
        option1_entry_2.insert(0, A[0][1])
        option2_entry_2.insert(0, A[0][2])
        option3_entry_2.insert(0, A[0][3])
        option4_entry_2.insert(0, A[0][4])
        crtoption_entry_2.insert(0, A[0][5])

        save_button_2 = Button(editor, text="Save",
                               command=lambda: update(question_entry_2.get(), option1_entry_2.get(),
                                                      option2_entry_2.get(), option3_entry_2.get(),
                                                      option4_entry_2.get(), crtoption_entry_2.get(), 2))
        save_button_2.grid(row=7, column=0, sticky=W)

        next_button_2 = Button(editor, text=">>", command=chgquestionthree)
        next_button_2.grid(row=7, column=1, sticky=E)

        conn.commit()
        conn.close()

    def chgquestionone():
        global Qno_1
        global question_1
        global option1_1
        global option2_1
        global option3_1
        global option4_1
        global crtoption_1
        global question_entry_1
        global option1_entry_1
        global option2_entry_1
        global option3_entry_1
        global option4_entry_1
        global crtoption_entry_1
        global save_button_1
        global next_button_1

        conn = sqlite3.connect("MCQDB")
        c = conn.cursor()

        Qno_1 = Label(editor, text="Question Number 1 - ")
        Qno_1.grid(row=0, column=0)

        question_1 = Label(editor, text="Question :")
        question_1.grid(row=1, column=0)

        option1_1 = Label(editor, text="Option 1 :")
        option1_1.grid(row=2, column=0)

        option2_1 = Label(editor, text="Option 2 :")
        option2_1.grid(row=3, column=0)

        option3_1 = Label(editor, text="Option 3 :")
        option3_1.grid(row=4, column=0)

        option4_1 = Label(editor, text="Option 4 :")
        option4_1.grid(row=5, column=0)

        crtoption_1 = Label(editor, text="Correct Option :")
        crtoption_1.grid(row=6, column=0)

        question_entry_1 = Entry(editor, width=30)
        question_entry_1.grid(row=1, column=1)

        option1_entry_1 = Entry(editor, width=30)
        option1_entry_1.grid(row=2, column=1)

        option2_entry_1 = Entry(editor, width=30)
        option2_entry_1.grid(row=3, column=1)

        option3_entry_1 = Entry(editor, width=30)
        option3_entry_1.grid(row=4, column=1)

        option4_entry_1 = Entry(editor, width=30)
        option4_entry_1.grid(row=5, column=1)

        crtoption_entry_1 = Entry(editor, width=30)
        crtoption_entry_1.grid(row=6, column=1)

        c.execute("SELECT * FROM MCQDB WHERE oid=" + str(1))
        A = c.fetchall()

        question_entry_1.insert(0, A[0][0])
        option1_entry_1.insert(0, A[0][1])
        option2_entry_1.insert(0, A[0][2])
        option3_entry_1.insert(0, A[0][3])
        option4_entry_1.insert(0, A[0][4])
        crtoption_entry_1.insert(0, A[0][5])

        save_button_1 = Button(editor, text="Save",
                               command=lambda: update(question_entry_1.get(), option1_entry_1.get(),
                                                      option2_entry_1.get(), option3_entry_1.get(),
                                                      option4_entry_1.get(), crtoption_entry_1.get(), 1))
        save_button_1.grid(row=7, column=0, sticky=W)

        next_button_1 = Button(editor, text=">>", command=chgquestiontwo)
        next_button_1.grid(row=7, column=1, sticky=E)

        conn.commit()
        conn.close()

    editor = Tk()
    editor.title("Question Editor")
    editor.resizable(0, 0)

    chgquestionone()

    editor.mainloop()


def submit():
    global score

    global question1_5
    global option1_5
    global option2_5
    global option3_5
    global option4_5
    global submitbutton

    question1_5.grid_forget()
    option1_5.grid_forget()
    option2_5.grid_forget()
    option3_5.grid_forget()
    option4_5.grid_forget()
    submitbutton.grid_forget()

    global tryagain
    global tryagain1
    global tryagainbutton

    if score >= 3:
        success = Label(root, text="Congratulation,You Scored {} / 5".format(score))
        success.grid(row=0, column=0)
    else:
        tryagain = Label(root, text="Try Again,You Only Scored {} / 5".format(score))
        tryagain.grid(row=0, column=0)
        tryagain1 = Label(root, text="Wanna Try Again?")
        tryagain1.grid(row=1, column=0)
        tryagainbutton = Button(root, text="Try Again", command=questionone)
        tryagainbutton.grid(row=2, column=0)


def questionfive():
    global score

    global question1_4
    global option1_4
    global option2_4
    global option3_4
    global option4_4
    global nextquestion_4

    question1_4.grid_forget()
    option1_4.grid_forget()
    option2_4.grid_forget()
    option3_4.grid_forget()
    option4_4.grid_forget()
    nextquestion_4.grid_forget()

    global question1_5
    global option1_5
    global option2_5
    global option3_5
    global option4_5
    global submitbutton

    conn = sqlite3.connect("MCQDB")
    c = conn.cursor()

    c.execute("SELECT * FROM MCQDB")
    first = c.fetchall()
    for i in first:
        firstQandA = first[4]
    question1_5 = Label(root, text=firstQandA[0])
    question1_5.grid(row=0, column=0, sticky=W, columnspan=1)

    a = IntVar()

    option1_5 = Radiobutton(root, text=firstQandA[1], variable=a, value=1)
    option1_5.grid(row=1, column=0, sticky=W, columnspan=1)
    option2_5 = Radiobutton(root, text=firstQandA[2], variable=a, value=2)
    option2_5.grid(row=2, column=0, sticky=W, columnspan=1)
    option3_5 = Radiobutton(root, text=firstQandA[3], variable=a, value=3)
    option3_5.grid(row=3, column=0, sticky=W, columnspan=1)
    option4_5 = Radiobutton(root, text=firstQandA[4], variable=a, value=4)
    option4_5.grid(row=4, column=0, sticky=W, columnspan=1)

    def solution(value):
        global score
        if value == firstQandA[5]:
            score += 1
        submit()

    submitbutton = Button(root, text="Submit", command=lambda: solution(a.get()))
    submitbutton.grid(row=5, column=1, sticky=W + E)

    conn.commit()
    conn.close()


def questionfour():

    global score

    global question1_3
    global option1_3
    global option2_3
    global option3_3
    global option4_3
    global nextquestion_3

    question1_3.grid_forget()
    option1_3.grid_forget()
    option2_3.grid_forget()
    option3_3.grid_forget()
    option4_3.grid_forget()
    nextquestion_3.grid_forget()

    global question1_4
    global option1_4
    global option2_4
    global option3_4
    global option4_4
    global nextquestion_4

    conn = sqlite3.connect("MCQDB")
    c = conn.cursor()

    c.execute("SELECT * FROM MCQDB")
    first = c.fetchall()
    for i in first:
        firstQandA = first[3]
    question1_4 = Label(root, text=firstQandA[0])
    question1_4.grid(row=0, column=0, sticky=W, columnspan=1)

    a = IntVar()

    option1_4 = Radiobutton(root, text=firstQandA[1], variable=a, value=1)
    option1_4.grid(row=1, column=0, sticky=W, columnspan=1)
    option2_4 = Radiobutton(root, text=firstQandA[2], variable=a, value=2)
    option2_4.grid(row=2, column=0, sticky=W, columnspan=1)
    option3_4 = Radiobutton(root, text=firstQandA[3], variable=a, value=3)
    option3_4.grid(row=3, column=0, sticky=W, columnspan=1)
    option4_4 = Radiobutton(root, text=firstQandA[4], variable=a, value=4)
    option4_4.grid(row=4, column=0, sticky=W, columnspan=1)

    def solution(value):
        global score
        if value == firstQandA[5]:
            score += 1
        questionfive()

    nextquestion_4 = Button(root, text=">>", command=lambda: solution(a.get()))
    nextquestion_4.grid(row=5, column=1, sticky=W)

    conn.commit()
    conn.close()


def questionthree():
    global score

    global question1_2
    global option1_2
    global option2_2
    global option3_2
    global option4_2
    global nextquestion_2

    question1_2.grid_forget()
    option1_2.grid_forget()
    option2_2.grid_forget()
    option3_2.grid_forget()
    option4_2.grid_forget()
    nextquestion_2.grid_forget()

    global question1_3
    global option1_3
    global option2_3
    global option3_3
    global option4_3
    global nextquestion_3

    conn = sqlite3.connect("MCQDB")
    c = conn.cursor()

    c.execute("SELECT * FROM MCQDB")
    first = c.fetchall()
    for i in first:
        firstQandA = first[2]
    question1_3 = Label(root, text=firstQandA[0])
    question1_3.grid(row=0, column=0, sticky=W, columnspan=1)

    a = IntVar()

    option1_3 = Radiobutton(root, text=firstQandA[1], variable=a, value=1)
    option1_3.grid(row=1, column=0, sticky=W, columnspan=1)
    option2_3 = Radiobutton(root, text=firstQandA[2], variable=a, value=2)
    option2_3.grid(row=2, column=0, sticky=W, columnspan=1)
    option3_3 = Radiobutton(root, text=firstQandA[3], variable=a, value=3)
    option3_3.grid(row=3, column=0, sticky=W, columnspan=1)
    option4_3 = Radiobutton(root, text=firstQandA[4], variable=a, value=4)
    option4_3.grid(row=4, column=0, sticky=W, columnspan=1)

    def solution(value):
        global score
        if value == firstQandA[5]:
            score += 1
        questionfour()

    nextquestion_3 = Button(root, text=">>", command=lambda: solution(a.get()))
    nextquestion_3.grid(row=5, column=1, sticky=W)

    conn.commit()
    conn.close()


def questiontwo():
    global score

    global question1
    global option1
    global option2
    global option3
    global option4
    global nextquestion_1

    question1.grid_forget()
    option1.grid_forget()
    option2.grid_forget()
    option3.grid_forget()
    option4.grid_forget()
    nextquestion_1.grid_forget()

    global question1_2
    global option1_2
    global option2_2
    global option3_2
    global option4_2
    global nextquestion_2

    conn = sqlite3.connect("MCQDB")
    c = conn.cursor()

    c.execute("SELECT * FROM MCQDB")
    first = c.fetchall()
    for i in first:
        firstQandA = first[1]
    question1_2 = Label(root, text=firstQandA[0])
    question1_2.grid(row=0, column=0, sticky=W, columnspan=1)

    a = IntVar()

    option1_2 = Radiobutton(root, text=firstQandA[1], variable=a, value=1)
    option1_2.grid(row=1, column=0, sticky=W, columnspan=1)
    option2_2 = Radiobutton(root, text=firstQandA[2], variable=a, value=2)
    option2_2.grid(row=2, column=0, sticky=W, columnspan=1)
    option3_2 = Radiobutton(root, text=firstQandA[3], variable=a, value=3)
    option3_2.grid(row=3, column=0, sticky=W, columnspan=1)
    option4_2 = Radiobutton(root, text=firstQandA[4], variable=a, value=4)
    option4_2.grid(row=4, column=0, sticky=W, columnspan=1)

    def solution(value):
        global score
        if value == firstQandA[5]:
            score += 1
        questionthree()

    nextquestion_2 = Button(root, text=">>", command=lambda: solution(a.get()))
    nextquestion_2.grid(row=5, column=1, sticky=W)

    conn.commit()
    conn.close()


def questionone():

    global score
    score = 0

    global question1
    global option1
    global option2
    global option3
    global option4
    global nextquestion_1

    Button1.grid_forget()
    Button2.grid_forget()
    Intro.grid_forget()

    try:
        global tryagain
        global tryagain1
        global tryagainbutton

        tryagain.grid_forget()
        tryagain1.grid_forget()
        tryagainbutton.grid_forget()

    except:
        pass

    conn = sqlite3.connect("MCQDB")
    c = conn.cursor()

    c.execute("SELECT * FROM MCQDB")
    first = c.fetchall()
    for i in first:
        firstQandA = first[0]
    question1 = Label(root, text=firstQandA[0])
    question1.grid(row=0, column=0, sticky=W, columnspan=1)

    a = IntVar()

    option1 = Radiobutton(root, text=firstQandA[1], variable=a, value=1)
    option1.grid(row=1, column=0, sticky=W, columnspan=1)
    option2 = Radiobutton(root, text=firstQandA[2], variable=a, value=2)
    option2.grid(row=2, column=0, sticky=W, columnspan=1)
    option3 = Radiobutton(root, text=firstQandA[3], variable=a, value=3)
    option3.grid(row=3, column=0, sticky=W, columnspan=1)
    option4 = Radiobutton(root, text=firstQandA[4], variable=a, value=4)
    option4.grid(row=4, column=0, sticky=W, columnspan=1)

    def solution(value):
        global score
        if value == firstQandA[5]:
            score += 1
        questiontwo()

    nextquestion_1 = Button(root, text=">>", command=lambda: solution(a.get()))
    nextquestion_1.grid(row=5, column=1, sticky=W)

    conn.commit()
    conn.close()


Font1 = font.Font(size=25)

Intro = Label(root, text="MCQ APPLICATION")
Intro['font'] = Font1
Intro.grid(row=0, column=0)

Button1 = Button(root, text="Start", command=questionone)
Button1.grid(row=1, column=0)

Button2 = Button(root, text="Change Questions", command=chgquestions)
Button2.grid(row=2, column=0)

conn.commit()
conn.close()

root.mainloop()