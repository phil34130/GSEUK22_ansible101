# Submit  Job

    from zoautil_py import jobs


    jcl_file = "/z/z04683/python/python.jcl"

    job_id = jobs.submit(jcl_file, is_unix=True)


    # Retrieve output

    job_dds: list[dict] = jobs.list_dds(job_id=job_id)

    raw_data: list[str] = job_dds["SYSUT2"].split("\n")

    return raw_data