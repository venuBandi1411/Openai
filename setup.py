from setuptools import setup, find_packages

setup(
    name='langchain-demo',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit>=0.88.0',
        'langchain-openai>=1.0.0',
        'langchain-community>=1.0.0'
    ],
    entry_points={
        'console_scripts': [
            'langchain-demo = langchain_demo.app:main'
        ]
    },
    author='Venu',
    author_email='venubandi001@email.com',
    description='Demo application using Langchain, Streamlit, OpenAI, and SerpAPI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Venubandi001/langchain-demo',
    license='MIT',
)
