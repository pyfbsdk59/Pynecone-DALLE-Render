import pynecone as pc

config = pc.Config(
    app_name="Pynecone_DALLE_Render",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
