class CourseNode:
    def __init__(self, course_title):
        self.course_title = course_title
        self.next = None

class CourseHistory:
    def __init__(self):
        self.head = None

    def add_course(self, course_title):
        new_node = CourseNode(course_title)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_history(self):
        history = []
        current = self.head
        while current:
            history.append(current.course_title)
            current = current.next
        return history
