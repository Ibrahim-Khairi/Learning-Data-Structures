class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.pointer = 0
        self.length = 1
        self.history_stack = [homepage]

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if len(self.history_stack) < self.pointer + 2:
            self.history_stack.append(url)
        else:
            self.history_stack[self.pointer + 1] = url
        self.pointer += 1
        self.length = self.pointer + 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.pointer = max(self.pointer - steps, 0)
        return self.history_stack[self.pointer]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.pointer = min(self.pointer + steps, len(self.history_stack) - 1)
        return self.history_stack[self.pointer]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# I did happen to watch a video on how to approach this problem, not because I couldn't really come up with a way, but because I didn't
# really know how to solve these kind of problems, which a class and multiple functions where we would have to use class-wide variables
# and stuff. Anyhow, the first approach they showed was a doubly-linked list which in my opinion is kind of easy, but the other one was
# this one. I have understood this therefore, I'll write down the explanation for this still.
# We are going to declare 3 properties/variables in the constructor. The first one will be the pointer. This will be the current URL at any
# given point in time that we are currently on. The second will be the length. This is the TRUE END of our array. This is NOT equal to
# len(array). The third one will be the history stack itself.
# First, I'll go over the forward and back functions since they are easier to explain.
# In back, we want to see whether our pointer - steps would be bigger than 0 or not.
# So imagine if the history looks like ["A", "B", "C", "D"], and we are currently at "D".
# We've been told to go 5 steps back. We can only realistically go 3 steps back to be at "A". Therefore if we do pointer (3) - 5, we'll get
# -2. 0 is bigger than that, so the amount of steps that we have to go back will automatically be set to 0 (meaning the current pointer will
# become 0. However, if we've been told to go 2 steps back, then it'll be 3-2, which is 1. Therefore, we'll end up at "B". So max kind of
# works like an if else statement here, but it's an easier trick. Will surely be implementing it in the future.
# Same thing happens with forward where we have to check it against the length - 1 (the total amount of URLs that are actually present
# within our history stack).
# Now moving on to visit, this is where it actually gets tricky. First, we need to see whether we are just straight away appending URLs, if
# we are at the latest page, or if we are actually overwriting our forward history, if we happen to be at one of the previous pages.
# We check that through the if else condition. len(self.history_stack) < self.pointer + 2 tells us whether the length of the stack is
# smaller than the slot next to pointer. Basically, what we are trying to see is - does pointer + 1 exist? The way that we can see whether
# anything exists is by doing length - 1 >= pointer. The reason why we do length - 1 is because, the last valid index is always 1 less than
# length. So that just becomes length >= pointer. If we want to see whether the slot next to pointer exists, then we just do length - 1 >=
# pointer + 1, which eventually becomes length >= pointer + 2. Finally, the reason why we are trying to see whether pointer + 1 exists is
# because we need to know whether there is forward history that needs to be overwritten. If there is none, meaning that length is actually
# smaller than pointer + 2 because we quite literally are at the most recent page, then we can just append it. Otherwise, if we are at one
# of the previous pages, then we'll just make the next slot that URL.
# After that, we'll increment the pointer by 1, and make the TRUE LENGTH of the stack that specific pointer + 1 since length is always one
# more than the biggest valid index, and the URL that we are appending right now is basically our most recent element, meaning the biggest
# index. However, this being said, there will be further stale URLs in the list too. So imagine if our history was
# ["A","B","C","D"], and we were currently at "B", now wanting to visit "E".
# Through our algorithm, we overwrite "C", so it becomes ["A","B","E","D"], however the "D" still remains the list, forever rotting in there,
# never being accounted or considered. This is because our TRUE LENGTH is denoted by self.length and not length(self.history_stack).