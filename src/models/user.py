class User:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def __eq__(self, other):
        if not isinstance(other, User):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name and self.job == other.job
