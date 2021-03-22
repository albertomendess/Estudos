import unittest
import python_repos as pr

class StatusTestCase(unittest.TestCase):
    """Testes para 'python_repos.py'."""

    def setUp(self):
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)

    def test_status_code(self):
        """Definindo se o Status Code do URL é 200."""
        self.assertEqual(self.r.status_code, 200)

    def test_repositories(self):
        """Desfinindo se todos os repositorios estão sendo tratados."""
        # Mostrar 30 repositorios.
        self.assertEqual(len(self.repo_dicts), 30)

        # Repositorios e suas chaves nescessárias.
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

unittest.main()