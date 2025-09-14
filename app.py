from load import pipeline
from load import export_to_s3

def lambda_handler(event, context):
    cmd = (event or {}).get("cmd", "pipeline")
    if cmd == "pipeline":
        pipeline.main()
    elif cmd == "export":
        export_to_s3.main()
    else:
        raise ValueError(f"Unknown cmd: {cmd}")
    return {"status":"ok", "cmd": cmd}