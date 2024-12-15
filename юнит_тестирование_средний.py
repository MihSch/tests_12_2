import runner
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = runner.Runner('Усэйн', 10)
        self.r2 = runner.Runner('Андрей', 9)
        self.r3 = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_run1(self):
        n = runner.Tournament(90, self.r1, self.r2, self.r3)
        res = runner.Tournament.start(n)
        self.all_results['test1'] = res

    def test_run2(self):
        n = runner.Tournament(90, self.r1, self.r2)
        res = runner.Tournament.start(n)
        self.all_results['test2'] = res

    def test_run3(self):
        n = runner.Tournament(90, self.r2, self.r3)
        res = runner.Tournament.start(n)
        self.all_results['test3'] = res

    def test_run4(self):
        n = runner.Tournament(90, self.r1, self.r3)
        res = runner.Tournament.start(n)
        self.all_results['test4'] = res