###############################################################################
# Auto-generated by `jupyter-book config`
# If you wish to continue using _config.yml, make edits to that file and
# re-generate this one.
###############################################################################
author = 'Gurobi Optimization'
comments_config = {'hypothesis': False, 'utterances': False}
copyright = '2025'
exclude_patterns = ['**.ipynb_checkpoints', '.DS_Store', 'Thumbs.db', '_build']
extensions = ['sphinx_togglebutton', 'sphinx_copybutton', 'myst_nb', 'jupyter_book', 'sphinx_thebe', 'sphinx_comments', 'sphinx_external_toc', 'sphinx.ext.intersphinx', 'sphinx_design', 'sphinx_book_theme', 'sphinx_jupyterbook_latex', 'sphinx_multitoc_numbering']
external_toc_exclude_missing = False
external_toc_path = '_toc.yml'
html_baseurl = ''
html_logo = 'logo.png'
html_sourcelink_suffix = ''

html_theme = 'gurobi_sphinxtheme'
html_favicon = 'https://www.gurobi.com/favicon.ico'

#html_theme = 'sphinx_book_theme'
#html_theme_options = {'search_bar_text': 'Search this book...', 'launch_buttons': {'notebook_interface': 'classic', 'binderhub_url': '', 'jupyterhub_url': '', 'thebe': False, 'colab_url': '', 'deepnote_url': ''}, 'path_to_docs': 'docs', 'repository_url': 'https://github.com/yurchisin/esups-supply-prepositioning', 'repository_branch': 'main', 'extra_footer': '', 'home_page_in_toc': True, 'announcement': '', 'analytics': {'google_analytics_id': '', 'plausible_analytics_domain': '', 'plausible_analytics_url': 'https://plausible.io/js/script.js'}, 'use_repository_button': True, 'use_edit_page_button': False, 'use_issues_button': True}
html_title = 'Optimization for Enhancing Humanitarian Aid'
latex_engine = 'pdflatex'
master_doc = 'content/intro'
myst_enable_extensions = ['colon_fence', 'dollarmath', 'linkify', 'substitution', 'tasklist']
myst_url_schemes = ['mailto', 'http', 'https']
nb_execution_allow_errors = False
nb_execution_cache_path = ''
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = 'force'
nb_execution_timeout = 30
nb_output_stderr = 'show'
numfig = True
pygments_style = 'sphinx'
suppress_warnings = ['myst.domains', 'mystnb.unknown_mime_type','mystnb.exec']
use_jupyterbook_latex = True
use_multitoc_numbering = True

# Allow errors so the build doesn’t stop
nbsphinx_allow_errors = True

# Display the entire traceback in the rendered HTML
nbsphinx_show_tracebacks = True