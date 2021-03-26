using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimationController : MonoBehaviour
{
    private bool isDamRaise = true;
    
    public Animator damAnimator;
    public Animator riverAnimator;

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (isDamRaise)
            {
                damAnimator.SetTrigger("Low");
                riverAnimator.SetTrigger("Raise");
                isDamRaise = false;
            }
            else
            {
                damAnimator.SetTrigger("Raise");
                riverAnimator.SetTrigger("Low");
                isDamRaise = true;
            }
        }
    }
}
