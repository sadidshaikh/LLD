from LLD.Stack_Overflow.StackOverflow import StackOverflow


class StackOverflowDemo:
    @staticmethod
    def run():
        system = StackOverflow()

        # Create users
        alice = system.create_user("Alice", "alice@example.com")
        bob = system.create_user("Bob", "bob@example.com")
        charlie = system.create_user("Charlie", "charlie@example.com")

        # ALice asks a question
        java_question = system.post_question(alice, "What is polymorphism in Java?",
                                             "Can someone explain polymorphism in Java with an example?",
                                             ["java", "oop"])

        # Bob answer Alice's question
        bob_answer = system.post_answer(bob, java_question,
                                        "Polymorphism in Java is the ability of an object to take on many forms...")

        # Charlie comments on the question
        system.add_comment(charlie, java_question, "Great question! I'm also interested in learning about this.")

        # Alice comments on Bob's answer
        system.add_comment(alice, bob_answer, "Thanks for the explanation! Could you provide a code example?")

        # Charlie votes on the question and answer
        system.add_vote(charlie, java_question, 1)
        system.add_vote(charlie, bob_answer, 1)

        # Alice accepts Bob's answer
        system.accept_answer(bob_answer)

        # Bob asks another question
        python_question = system.post_question(bob, "How to use list comprehensions in Python?",
                                               "I'm new to Python and I've heard about list comprehensions. Can someone explain how to use them?",
                                               ["python", "list-comprehension"])

        # Alice answers Bob's question
        alice_answer = system.post_answer(alice, python_question,
                                          "List comprehensions in Python provide a concise way to create lists...")

        # Charlie votes on the question and answer
        system.add_vote(charlie, python_question, 1)
        system.add_vote(charlie, alice_answer, 1)

        # Print out the current state
        print(f"Question: {java_question.title}")
        print(f"Asked by: {java_question.author.username}")
        print(f"Tags: {','.join(tag.name for tag in java_question.tags)}")
        print(f"Votes: {java_question.get_vote_count()}")
        print(f"Comments: {len(java_question.get_comments())}")
        print(f"\nAnswer by: {bob_answer.author.username}")
        print(bob_answer.content)
        print(f"Votes: {bob_answer.get_vote_count()}")
        print(f"Accepted: {bob_answer.is_accepted}")
        print(f"Comments: {len(bob_answer.get_comments())}")

        print("\nUser Reputations:")
        print(f"Alice: {alice.reputation}")
        print(f"Bob: {bob.reputation}")
        print(f"Charlie: {charlie.reputation}")

        # Demonstrate search functionality
        print("\nSearch results for 'java':")
        search_results = system.search_question("jav")
        for q in search_results:
            print(q.title)

        print("\nSearch results for 'python':")
        search_results = system.search_question("python")
        for q in search_results:
            print(q.title)

        # Demonstrate getting question by User
        print("\nBob's Questions:")
        bob_questions = system.get_questions_by_user(bob)
        for q in bob_questions:
            print(q.title)
